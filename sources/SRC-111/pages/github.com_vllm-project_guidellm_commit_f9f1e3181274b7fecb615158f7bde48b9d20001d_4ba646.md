source: https://github.com/vllm-project/guidellm/commit/f9f1e3181274b7fecb615158f7bde48b9d20001d

@@ -389,6 +389,8 @@ class TestAsyncConstantStrategy:


`389`

`389`

{"rate" : 1.0 },


`390`

`390`

{"rate" : 5.0 },


`391`

`391`

{"rate" : 10.3 , "max_concurrency" : 8 },



`392`

+ {"rate" : 2.0 , "rampup_duration" : 1.0 },



`393`

+ {"rate" : 10.0 , "rampup_duration" : 2.0 , "max_concurrency" : 5 },


`392`

`394`

]


`393`

`395`

)


`394`

`396`

def valid_instances (self , request ):


@@ -412,6 +414,7 @@ def test_initialization(self, valid_instances: tuple[AsyncConstantStrategy, dict


`412`

`414`

[


`413`

`415`

("rate" , 0 ),


`414`

`416`

("rate" , - 1.0 ),



`417`

+ ("rampup_duration" , - 1.0 ),


`415`

`418`

],


`416`

`419`

)


`417`

`420`

def test_invalid_initialization (self , field , value ):


@@ -473,6 +476,180 @@ def test_marshalling(self, valid_instances: tuple[AsyncConstantStrategy, dict]):


`473`

`476`

for key , value in constructor_args .items ():


`474`

`477`

assert getattr (base_json_reconstructed , key ) == value


`475`

`478`




`479`

+ @pytest .mark .smoke



`480`

+ def test_rampup_duration_default (self ):



`481`

+ """Test that rampup_duration defaults to 0.0.



`482`

+



`483`

+ ### WRITTEN BY AI ###



`484`

+ """



`485`

+ instance = AsyncConstantStrategy (rate = 1.0 )



`486`

+ assert instance .rampup_duration == 0.0



`487`

+



`488`

+ @pytest .mark .smoke



`489`

+ def test_rampup_duration_initialization (self ):



`490`

+ """Test that rampup_duration can be set.



`491`

+



`492`

+ ### WRITTEN BY AI ###



`493`

+ """



`494`

+ instance = AsyncConstantStrategy (rate = 10.0 , rampup_duration = 2.0 )



`495`

+ assert instance .rampup_duration == 2.0



`496`

+



`497`

+ @pytest .mark .smoke



`498`

+ @pytest .mark .asyncio



`499`

+ async def test_timing_without_rampup (self ):



`500`

+ """Test timing without rampup matches existing behavior.



`501`

+



`502`

+ ### WRITTEN BY AI ###



`503`

+ """



`504`

+ strategy = AsyncConstantStrategy (rate = 10.0 , rampup_duration = 0.0 )



`505`

+ strategy .init_processes_timings (worker_count = 1 , max_concurrency = 100 )



`506`

+ start_time = 1000.0



`507`

+ strategy .init_processes_start (start_time )



`508`

+



`509`

+ # Test multiple request indices



`510`

+ # Each call to next_request_time increments the index automatically



`511`

+ for expected_index in range (1 , 11 ):



`512`

+ time = await strategy .next_request_time (0 )



`513`

+ expected_time = start_time + expected_index / 10.0



`514`

+ assert time == pytest .approx (expected_time , rel = 1e-10 ), (



`515`

+ f"Request { expected_index } : expected { expected_time } , got { time } "



`516`

+ )



`517`

+



`518`

+ @pytest .mark .smoke



`519`

+ @pytest .mark .asyncio



`520`

+ async def test_timing_with_rampup (self ):



`521`

+ """Test timing with rampup follows quadratic then linear pattern.



`522`

+



`523`

+ ### WRITTEN BY AI ###



`524`

+ """



`525`

+ rate = 10.0



`526`

+ rampup_duration = 2.0



`527`

+ strategy = AsyncConstantStrategy (rate = rate , rampup_duration = rampup_duration )



`528`

+ strategy .init_processes_timings (worker_count = 1 , max_concurrency = 100 )



`529`

+ start_time = 1000.0



`530`

+ strategy .init_processes_start (start_time )



`531`

+



`532`

+ # Calculate number of requests during rampup



`533`

+ n_rampup = rate * rampup_duration / 2.0 # Should be 10



`534`

+



`535`

+ # Test first request (index 1) - should be at start_time



`536`

+ time1 = await strategy .next_request_time (0 )



`537`

+ assert time1 == pytest .approx (start_time , abs = 1e-6 ), (



`538`

+ f"First request should be at start_time, got { time1 } "



`539`

+ )



`540`

+



`541`

+ # Test requests during rampup (indices 2-10)



`542`

+ # For index n during rampup: t = sqrt(2 * n * rampup_duration / rate)



`543`

+ # Each call increments the index automatically



`544`

+ for n in range (2 , int (n_rampup ) + 1 ):



`545`

+ time_n = await strategy .next_request_time (0 )



`546`

+ expected_time = start_time + math .sqrt (2.0 * n * rampup_duration / rate )



`547`

+ assert time_n == pytest .approx (expected_time , rel = 1e-6 ), (



`548`

+ f"Request { n } during rampup: expected { expected_time } , got { time_n } "



`549`

+ )



`550`

+



`551`

+ # Test request right after rampup (index 11)



`552`

+ # Should be at: rampup_duration + (11 - n_rampup) / rate



`553`

+ time_after = await strategy .next_request_time (0 )



`554`

+ expected_after = start_time + rampup_duration + (11 - n_rampup ) / rate



`555`

+ assert time_after == pytest .approx (expected_after , rel = 1e-6 ), (



`556`

+ f"Request 11 after rampup: expected { expected_after } , got { time_after } "



`557`

+ )



`558`

+



`559`

+ # Test a few more requests after rampup to verify constant rate



`560`

+ for i in range (12 , 15 ):



`561`

+ time_i = await strategy .next_request_time (0 )



`562`

+ expected_i = start_time + rampup_duration + (i - n_rampup ) / rate



`563`

+ assert time_i == pytest .approx (expected_i , rel = 1e-6 ), (



`564`

+ f"Request { i } after rampup: expected { expected_i } , got { time_i } "



`565`

+ )



`566`

+



`567`

+ @pytest .mark .sanity



`568`

+ @pytest .mark .asyncio



`569`

+ async def test_timing_with_rampup_edge_cases (self ):



`570`

+ """Test edge cases for rampup timing.



`571`

+



`572`

+ ### WRITTEN BY AI ###



`573`

+ """



`574`

+



`575`

+ # Test with very short rampup_duration



`576`

+ strategy = AsyncConstantStrategy (rate = 100.0 , rampup_duration = 0.01 )



`577`

+ strategy .init_processes_timings (worker_count = 1 , max_concurrency = 100 )



`578`

+ start_time = 2000.0



`579`

+ strategy .init_processes_start (start_time )



`580`

+



`581`

+ # First request



`582`

+ time1 = await strategy .next_request_time (0 )



`583`

+ assert time1 == pytest .approx (start_time , abs = 1e-6 )



`584`

+



`585`

+ # Test with very long rampup_duration



`586`

+ strategy2 = AsyncConstantStrategy (rate = 1.0 , rampup_duration = 100.0 )



`587`

+ strategy2 .init_processes_timings (worker_count = 1 , max_concurrency = 100 )



`588`

+ start_time2 = 3000.0



`589`

+ strategy2 .init_processes_start (start_time2 )



`590`

+



`591`

+ # First request



`592`

+ time1_2 = await strategy2 .next_request_time (0 )



`593`

+ assert time1_2 == pytest .approx (start_time2 , abs = 1e-6 )



`594`

+



`595`

+ # Request at end of rampup



`596`

+ # We need to advance to request index 50 (n_rampup = 1.0 * 100.0 / 2.0)



`597`

+ # Already at index 1, need 49 more calls to reach index 50



`598`

+ time_end_rampup = None



`599`

+ for _ in range (49 ): # 49 calls to go from index 2 to index 50



`600`

+ time_end_rampup = await strategy2 .next_request_time (0 )



`601`

+ expected_end = start_time2 + 100.0



`602`

+ assert time_end_rampup == pytest .approx (expected_end , rel = 1e-6 ), (



`603`

+ f"End of rampup: expected { expected_end } , got { time_end_rampup } "



`604`

+ )



`605`

+



`606`

+ @pytest .mark .sanity



`607`

+ @pytest .mark .asyncio



`608`

+ async def test_timing_rampup_transition (self ):



`609`

+ """Test smooth transition from rampup to constant rate.



`610`

+



`611`

+ ### WRITTEN BY AI ###



`612`

+ """



`613`

+ rate = 10.0



`614`

+ rampup_duration = 2.0



`615`

+ strategy = AsyncConstantStrategy (rate = rate , rampup_duration = rampup_duration )



`616`

+ strategy .init_processes_timings (worker_count = 1 , max_concurrency = 100 )



`617`

+ start_time = 5000.0



`618`

+ strategy .init_processes_start (start_time )



`619`

+



`620`

+ n_rampup = rate * rampup_duration / 2.0 # 10



`621`

+



`622`

+ # Get to the last request of rampup (index 10)



`623`

+ for _ in range (9 ): # Already at index 1, need 9 more to reach 10



`624`

+ await strategy .next_request_time (0 )



`625`

+



`626`

+ time_last_rampup = await strategy .next_request_time (0 )



`627`

+ expected_last_rampup = start_time + math .sqrt (



`628`

+ 2.0 * 10 * rampup_duration / rate



`629`

+ )



`630`

+ assert time_last_rampup == pytest .approx (



`631`

+ expected_last_rampup , rel = 1e-6



`632`

+ ), (



`633`

+ f"Last rampup request: expected { expected_last_rampup } , "



`634`

+ f"got { time_last_rampup } "



`635`

+ )



`636`

+



`637`

+ # First request after rampup (index 11)



`638`

+ time_first_after = await strategy .next_request_time (0 )



`639`

+ expected_first_after = start_time + rampup_duration + (11 - n_rampup ) / rate



`640`

+ assert time_first_after == pytest .approx (



`641`

+ expected_first_after , rel = 1e-6



`642`

+ ), (



`643`

+ f"First after rampup: expected { expected_first_after } , "



`644`

+ f"got { time_first_after } "



`645`

+ )



`646`

+



`647`

+ # Verify the transition is smooth (no gap)



`648`

+ # The last rampup request should be at rampup_duration



`649`

+ assert time_last_rampup == pytest .approx (



`650`

+ start_time + rampup_duration , rel = 1e-6



`651`

+ ), "Last rampup should be at end of rampup period"



`652`

+


`476`

`653`



`477`

`654`

class TestAsyncPoissonStrategy :


`478`

`655`

@pytest .fixture (


## 0 commit comments