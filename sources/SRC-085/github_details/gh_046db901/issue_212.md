# [Issue #212] EAGLE3-LLaMA3.1-Instruct-8B outputs are inconsistent with autoregressive (naive) decoding with temperature=0

source: https://github.com/SafeAILab/EAGLE/issues/212
state: closed | updated: 2025-06-04T03:23:41Z
labels: 

## 正文

Hello, I noticed that the output of EAGLE3 differs from the naive baseline. Out of 80 prompts in MT-benchmark, only 50 match exactly while the rest can significantly differ.

Below is an example of visualized alignment of 1 sample from MT-bench, where **REF:** corresponds to auto-regressive decoding and **HYP:** to EAGLE-3.

[jiwer](https://jitsi.github.io/jiwer/usage/#alignment) was used for alignment visualization.

My typical mean word error-rate on `MT-benchmark` is 0.14 (14%), when it's expected to be 0.0 with temperature 0.0. This expectation holds for multiple runs of naive decoding but fails for EAGLE-3. What might be the reason for such behavior?

I noticed that EAGLE's token set can differ from the base model's token set (https://github.com/SafeAILab/EAGLE/blob/main/eagle/model/cnets.py#L699) and I wonder if that could be causing this discrepancy. On the other hand, if that were the reason, then the draft sequence would not be accepted by the target model. Can you clarify why the generated sequences do not match?

Interestingly, multiple re-runs of EAGLE-3 inference produce exactly the same outputs, and all of them have systematic misalignment with the baseline.

I'm running inference with this script:

```
  python eagle/evaluation/gen_ea_answer_llama3chat.py \
    --depth 8 \
    --max-new-token 2048 \
    --use-eagle3 \
    --model-id eagle3-llama3.1-instruct-8b-temperature-0.0-topk-depth-${d}.jsonl
```


```
=== SENTENCE 1 ===

REF: I'd be happy to explain the differences between exothermic and endothermic reactions. **What are Exothermic and Endothermic Reactions?** ** ********** * ******** ** * ******* ** ***** *** ** **** ********** *********** *** ********* **** *** ********
** *********** Exothermic and endothermic reactions are two types of chemical reactions that  occur in different     ways, releasing     or absorbing energy. **Exothermic Reactions:** ** ********** Exothermic reactions are chemical reactions that  release
 energy into the surroundings. This energy is usually in the form of heat, light, or sound. **** **** The reaction is ***** characterized by a decrease in          the potential energy       of    the reactants,  resulting       in an increase in the ****
 ** ***** ***** *** potential   energy    of the surroundings. **Criteria to Distinguish Exothermic Reactions:** To identify an exothermic reaction, look for the following criteria: 1. **Heat is released**: The reaction produces heat,  which  can  be
        felt or measured using a thermometer.
2. **Temperature increases**: The temperature of the surroundings increases as a result of the reaction.
3. **Energy is released**: The reaction releases energy in the form of heat, light, or sound. **Endothermic Reactions:** ** *********** Endothermic reactions are chemical reactions that  absorb energy from the surroundings. This energy is usually in the f
orm of heat, light, or sound. **** **** The reaction is ***** characterized by an increase in          the potential energy       of    the reactants,   resulting       in  a decrease in the **** ** ***** ***** *** potential   energy    of the surrounding
s. **Criteria to Distinguish Endothermic Reactions:** To identify an endothermic reaction, look for the following criteria: 1. **Heat is absorbed**: The reaction absorbs heat ****** from the surroundings.
2. **Temperature decreases**: The temperature of the surroundings decreases as a result of the reaction.
3. **Energy is absorbed**: The reaction absorbs energy in the form of heat, light, or sound. **Real-World Example:** A classic example of an exothermic reaction is the combustion of gasoline in a car engine. When gasoline is burned, it releases a large am
ount of energy in the form of heat and light, which is used to power the car. This reaction is characterized      by  a decrease in the potential energy   of the gasoline and an increase in the potential energy of the surroundings. On the other hand, a cl
assic example of an endothermic reaction is the melting of ice. When ice is heated, it absorbs energy from the surroundings in the form of heat, causing the temperature to decrease. This reaction is characterized      by an increase in the potential energ
y   of the          ice and a decrease in the potential energy of the surroundings. In summary, exothermic reactions release
HYP: I'd be happy to explain the differences between exothermic and endothermic reactions. **What are Exothermic and Endothermic Reactions?** In chemistry, a reaction is a process in which one or more substances (reactants) are converted into new substanc
es (products). Exothermic and endothermic reactions are two types of chemical reactions that differ in       the direction        of energy transfer. ******* **Exothermic Reactions:** An exothermic   reaction        is   a chemical  reaction that releases
 energy into the  surroundings **** ****** ** ******* in the form of heat, light, or sound. This type  of reaction is often   accompanied by a decrease in temperature.       The energy released during         an exothermic reaction is  usually in the form
 of heat, which can        be measured using   a  thermometer. **Criteria to Distinguish Exothermic Reactions:** To identify an exothermic reaction, look for the following criteria: 1. **Heat is released**: The reaction releases  heat energy into the surr
oundings.
2. ** ******** ***** * *************** **Temperature decreases**: The temperature of the surroundings decreases as a result of the reaction.
3. **Energy is released**: The reaction releases energy in the form of heat, light, or sound. **Endothermic Reactions:** An endothermic    reaction        is   a chemical  reaction that absorbs energy from the  surroundings **** ****** ** ******* in the f
orm of heat, light, or sound. This type  of reaction is often   accompanied by an increase in temperature.       The energy absorbed during         an endothermic reaction is  usually in the form of heat, which can        be measured using   a  thermomete
r. **Criteria to Distinguish Endothermic Reactions:** To identify an endothermic reaction, look for the following criteria: 1. **Heat is absorbed**: The reaction absorbs heat energy from the surroundings.
2. **Temperature increases**: The temperature of the surroundings increases as a result of the reaction.
3. **Energy is absorbed**: The reaction absorbs energy in the form of heat, light, or sound. **Real-World Example:** A classic example of an exothermic reaction is the combustion of gasoline in a car engine. When gasoline is burned, it releases a large am
ount of energy in the form of heat and light, which is used to power the car. This reaction is    exothermic because it releases ** *** ********* energy into the ******** *** ** ******** ** *** ********* ****** ** *** surroundings. On the other hand, a cl
assic example of an endothermic reaction is the melting of ice. When ice is heated, it absorbs energy from the surroundings in the form of heat, causing the temperature to increase. This reaction is   endothermic because it  absorbs ** *** ********* energ
y from the surroundings *** * ******** ** *** ********* ****** ** *** ************* ** ******** ********** ********* *******
                                                                                                                                               I          I I        I  I I       I  I     I   I  I    I          I           I   I         I    I   I
 I           I                                                                                    S            S         S         S      S         S       D                            I          I          S         S   S                  S             S
                             S    D      D  D       D                                          I    I   S                 I             S                             S         S               S      S          S          S        S  S        S           I
  I     I     I   I         S        S     S   S             S                                                                                                                                                                     S     S      S    S   S
           S  D        D     D D               D                          S                                             S
                  I           I           S         S   S                  S            S                             S    D      D  D       D                                          I    I   S                 I             S
 S         S               S      S          S           S        S  S        S           I  I     I     I   I         S        S     S   S             S
                                                                            I                                                    S                                             S

                                                          S       S  S        S  D   D         D           S            D   D  D        D  D   D         D      D  D   D
                                                                                                                                   S                              S       S  S        S  D   D         D           S                S   D D        D  D   D
     D      D  D   D             D  D        D          D         D       D

=== SENTENCE 2 ===

REF: Yes, a process can involve both exothermic and endothermic reactions. This is known as a **coupled reaction** or **combined reaction**. **Example:** A classic example of a process that involves both exothermic and endothermic reactions is the **photo
synthesis** process in plants. **Photosynthesis:** Photosynthesis is the process by which plants convert light energy from the sun into chemical energy in the form of glucose. This process involves two main stages: 1. **Light-dependent reactions** (exothe
rmic): In this stage, light energy is absorbed by pigments such as chlorophyll and converted into ATP and NADPH. This process releases energy in the form of heat and light.
2. **Light-independent reactions** (Calvin cycle, endothermic): In this stage, CO2 is fixed into glucose using the energy from ATP and NADPH produced in the light-dependent reactions. This process absorbs energy from the surroundings in the form of light
and heat. In *************** summary,  photosynthesis  involves both  exothermic (light-dependent)    and endothermic (Calvin        cycle) reactions, demonstrating              that         a process          can   involve   both types  of    reactions.
This ** ** example ** * ******* ********* ***** *** ********* ***** ******** illustrates     how a *** ******* complex process **       can involve multiple reactions,   some of which      are exothermic and ******* ********* *** ****** others that are en
dothermic.
HYP: Yes, a process can involve both exothermic and endothermic reactions. This is known as a **coupled reaction** or **combined reaction**. **Example:** A classic example of a process that involves both exothermic and endothermic reactions is the **photo
synthesis** process in plants. **Photosynthesis:** Photosynthesis is the process by which plants convert light energy from the sun into chemical energy in the form of glucose. This process involves two main stages: 1. **Light-dependent reactions** (exothe
rmic): In this stage, light energy is absorbed by pigments such as chlorophyll and converted into ATP and NADPH. This process releases energy in the form of heat and light.
2. **Light-independent reactions** (Calvin cycle, endothermic): In this stage, CO2 is fixed into glucose using the energy from ATP and NADPH produced in the light-dependent reactions. This process absorbs energy from the surroundings in the form of light
and heat. In photosynthesis,      the light-dependent reactions  are exothermic,         releasing energy        into     the surroundings,      while           the light-independent reactions     are endothermic, absorbing energy  from the surroundings.
This is an example of a coupled reaction, where two reactions occur together          to produce a net result.    This process is essential     for     life         on Earth, as    it provides     energy and organic compounds for plants     to grow and
   thrive.



                                                                                                                                                                                                        I        S               S         S    S           S
               S      S           S       S             S          S             S                 S         S       S            S         S      S     S   S             S       I  I          I I       I         I     I   I         I     I        I
     S       S     I       I       S          I         S       S        S          S      S  S     S        S          S           I         I   I      I      S    S   S            S


=== SUMMARY ===
number of sentences: 2
substitutions=109 deletions=45 insertions=60 hits=414

mer=34.08%
wil=48.24%
wip=51.76%
wer=37.68%
```





## 评论 (1)

### hongyanz · 2025-05-19

@taras-sereda Please check the second bullet in this answer. We believe it is not an issue of EAGLE, but the phenomenon happens quite often. OpenAI reported the same issue before.

https://github.com/vllm-project/vllm/issues/5404#issuecomment-2788169480
