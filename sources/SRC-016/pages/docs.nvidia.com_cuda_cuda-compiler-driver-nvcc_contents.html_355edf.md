source: https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/contents.html

# Contents[](https://docs.nvidia.com#contents)

-
[1. Introduction](https://docs.nvidia.com/index.html) -
[2. Compilation Phases](https://docs.nvidia.com/index.html#compilation-phases) [3. The CUDA Compilation Trajectory](https://docs.nvidia.com/index.html#the-cuda-compilation-trajectory)-
[4. NVCC Command Options](https://docs.nvidia.com/index.html#nvcc-command-options)[4.1. Command Option Types and Notation](https://docs.nvidia.com/index.html#command-option-types-and-notation)-
[4.2. Command Option Description](https://docs.nvidia.com/index.html#command-option-description)-
[4.2.1. File and Path Specifications](https://docs.nvidia.com/index.html#file-and-path-specifications)[4.2.1.1.](https://docs.nvidia.com/index.html#output-file-file-o)`--output-file file`

(`-o`

)[4.2.1.2.](https://docs.nvidia.com/index.html#objdir-as-tempdir-objtemp)`--objdir-as-tempdir`

(`-objtemp`

)[4.2.1.3.](https://docs.nvidia.com/index.html#pre-include-file-include)`--pre-include file,...`

(`-include`

)[4.2.1.4.](https://docs.nvidia.com/index.html#library-library-l)`--library library,...`

(`-l`

)[4.2.1.5.](https://docs.nvidia.com/index.html#define-macro-def-d)`--define-macro def,...`

(`-D`

)[4.2.1.6.](https://docs.nvidia.com/index.html#undefine-macro-def-u)`--undefine-macro def,...`

(`-U`

)[4.2.1.7.](https://docs.nvidia.com/index.html#include-path-path-i)`--include-path path,...`

(`-I`

)[4.2.1.8.](https://docs.nvidia.com/index.html#system-include-path-isystem)`--system-include path,...`

(`-isystem`

)[4.2.1.9.](https://docs.nvidia.com/index.html#library-path-path-l)`--library-path path,...`

(`-L`

)[4.2.1.10.](https://docs.nvidia.com/index.html#output-directory-directory-odir)`--output-directory directory`

(`-odir`

)[4.2.1.11.](https://docs.nvidia.com/index.html#dependency-output-file-mf)`--dependency-output file`

(`-MF`

)[4.2.1.12.](https://docs.nvidia.com/index.html#generate-dependency-targets-mp)`--generate-dependency-targets`

(`-MP`

)[4.2.1.13.](https://docs.nvidia.com/index.html#compiler-bindir-directory-ccbin)`--compiler-bindir directory`

(`-ccbin`

)[4.2.1.14.](https://docs.nvidia.com/index.html#allow-unsupported-compiler-allow-unsupported-compiler)`--allow-unsupported-compiler`

(`-allow-unsupported-compiler`

)[4.2.1.15.](https://docs.nvidia.com/index.html#archiver-binary-executable-arbin)`--archiver-binary executable`

(`-arbin`

)[4.2.1.16.](https://docs.nvidia.com/index.html#cudart-none-shared-static-hybrid-cudart)`--cudart`

{`none`

|`shared`

|`static`

|`hybrid`

} (`-cudart`

)[4.2.1.17.](https://docs.nvidia.com/index.html#cudadevrt-none-static-cudadevrt)`--cudadevrt`

{`none`

|`static`

} (`-cudadevrt`

)[4.2.1.18.](https://docs.nvidia.com/index.html#libdevice-directory-directory-ldir)`--libdevice-directory directory`

(`-ldir`

)[4.2.1.19.](https://docs.nvidia.com/index.html#target-directory-string-target-dir)`--target-directory string`

(`-target-dir`

)[4.2.1.20.](https://docs.nvidia.com/index.html#apply-controls-apply-controls)`--apply-controls`

(`-apply-controls`

)

-
[4.2.2. Options for Specifying the Compilation Phase](https://docs.nvidia.com/index.html#options-for-specifying-the-compilation-phase)[4.2.2.1.](https://docs.nvidia.com/index.html#link-link)`--link`

(`-link`

)[4.2.2.2.](https://docs.nvidia.com/index.html#lib-lib)`--lib`

(`-lib`

)[4.2.2.3.](https://docs.nvidia.com/index.html#device-link-dlink)`--device-link`

(`-dlink`

)[4.2.2.4.](https://docs.nvidia.com/index.html#device-c-dc)`--device-c`

(`-dc`

)[4.2.2.5.](https://docs.nvidia.com/index.html#device-w-dw)`--device-w`

(`-dw`

)[4.2.2.6.](https://docs.nvidia.com/index.html#cuda-cuda)`--cuda`

(`-cuda`

)[4.2.2.7.](https://docs.nvidia.com/index.html#compile-c)`--compile`

(`-c`

)[4.2.2.8.](https://docs.nvidia.com/index.html#fatbin-fatbin)`--fatbin`

(`-fatbin`

)[4.2.2.9.](https://docs.nvidia.com/index.html#cubin-cubin)`--cubin`

(`-cubin`

)[4.2.2.10.](https://docs.nvidia.com/index.html#ptx-ptx)`--ptx`

(`-ptx`

)[4.2.2.11.](https://docs.nvidia.com/index.html#tilefatbin-tilefatbin)`--tilefatbin`

(`-tilefatbin`

)[4.2.2.12.](https://docs.nvidia.com/index.html#tilecubin-tilecubin)`--tilecubin`

(`-tilecubin`

)[4.2.2.13.](https://docs.nvidia.com/index.html#tilebc-tilebc)`--tilebc`

(`-tilebc`

)[4.2.2.14.](https://docs.nvidia.com/index.html#preprocess-e)`--preprocess`

(`-E`

)[4.2.2.15.](https://docs.nvidia.com/index.html#generate-dependencies-m)`--generate-dependencies`

(`-M`

)[4.2.2.16.](https://docs.nvidia.com/index.html#generate-nonsystem-dependencies-mm)`--generate-nonsystem-dependencies`

(`-MM`

)[4.2.2.17.](https://docs.nvidia.com/index.html#generate-dependencies-with-compile-md)`--generate-dependencies-with-compile`

(`-MD`

)[4.2.2.18.](https://docs.nvidia.com/index.html#generate-nonsystem-dependencies-with-compile-mmd)`--generate-nonsystem-dependencies-with-compile`

(`-MMD`

)[4.2.2.19.](https://docs.nvidia.com/index.html#optix-ir-optix-ir)`--optix-ir`

(`-optix-ir`

)[4.2.2.20.](https://docs.nvidia.com/index.html#ltoir-ltoir)`--ltoir`

(`-ltoir`

)[4.2.2.21.](https://docs.nvidia.com/index.html#run-run)`--run`

(`-run`

)

-
[4.2.3. Options for Specifying Behavior of Compiler/Linker](https://docs.nvidia.com/index.html#options-for-specifying-behavior-of-compiler-linker)[4.2.3.1.](https://docs.nvidia.com/index.html#enable-tile-enable-tile)`--enable-tile`

(`-enable-tile`

)[4.2.3.2.](https://docs.nvidia.com/index.html#tile-only-tile-only)`--tile-only`

(`-tile-only`

)[4.2.3.3.](https://docs.nvidia.com/index.html#simt-only-simt-only)`--simt-only`

(`-simt-only`

)[4.2.3.4.](https://docs.nvidia.com/index.html#profile-pg)`--profile`

(`-pg`

)[4.2.3.5.](https://docs.nvidia.com/index.html#debug-g)`--debug`

(`-g`

)[4.2.3.6.](https://docs.nvidia.com/index.html#device-debug-g)`--device-debug`

(`-G`

)[4.2.3.7.](https://docs.nvidia.com/index.html#extensible-whole-program-ewp)`--extensible-whole-program`

(`-ewp`

)[4.2.3.8.](https://docs.nvidia.com/index.html#no-compress-no-compress)`--no-compress`

(`-no-compress`

)[4.2.3.9.](https://docs.nvidia.com/index.html#compress-mode-default-size-speed-balance-none-compress-mode)`--compress-mode`

{`default`

|`size`

|`speed`

|`balance`

|`none`

} (`-compress-mode`

)[4.2.3.10.](https://docs.nvidia.com/index.html#concat-concat)`--concat`

(`-concat`

)[4.2.3.11.](https://docs.nvidia.com/index.html#relocatable-ptx-reloc-ptx)`--relocatable-ptx`

(`-reloc-ptx`

)[4.2.3.12.](https://docs.nvidia.com/index.html#generate-line-info-lineinfo)`--generate-line-info`

(`-lineinfo`

)[4.2.3.13.](https://docs.nvidia.com/index.html#optimization-info-kind-opt-info)`--optimization-info kind,...`

(`-opt-info`

)[4.2.3.14.](https://docs.nvidia.com/index.html#optimize-level-o)`--optimize level`

(`-O`

)[4.2.3.15.](https://docs.nvidia.com/index.html#ofast-compile-level-ofc)`--Ofast-compile level`

(`-Ofc`

)[4.2.3.16.](https://docs.nvidia.com/index.html#dopt-kind-dopt)`--dopt kind`

(`-dopt`

)[4.2.3.17.](https://docs.nvidia.com/index.html#dlink-time-opt-dlto)`--dlink-time-opt`

(`-dlto`

)[4.2.3.18.](https://docs.nvidia.com/index.html#gen-opt-lto-gen-opt-lto)`--gen-opt-lto`

(`-gen-opt-lto`

)[4.2.3.19.](https://docs.nvidia.com/index.html#split-compile-number-split-compile)`--split-compile number`

(`-split-compile`

)[4.2.3.20.](https://docs.nvidia.com/index.html#split-compile-extended-number-split-compile-extended)`--split-compile-extended number`

(`-split-compile-extended`

)[4.2.3.21.](https://docs.nvidia.com/index.html#jobserver-jobserver)`--jobserver`

(`-jobserver`

)[4.2.3.22.](https://docs.nvidia.com/index.html#skip-ptx-semantics-check-skip-ptx-semantics-check)`--skip-ptx-semantics-check`

(`-skip-ptx-semantics-check`

)[4.2.3.23.](https://docs.nvidia.com/index.html#ftemplate-backtrace-limit-limit-ftemplate-backtrace-limit)`--ftemplate-backtrace-limit limit`

(`-ftemplate-backtrace-limit`

)[4.2.3.24.](https://docs.nvidia.com/index.html#ftemplate-depth-limit-ftemplate-depth)`--ftemplate-depth limit`

(`-ftemplate-depth`

)[4.2.3.25.](https://docs.nvidia.com/index.html#no-exceptions-noeh)`--no-exceptions`

(`-noeh`

)[4.2.3.26.](https://docs.nvidia.com/index.html#shared-shared)`--shared`

(`-shared`

)[4.2.3.27.](https://docs.nvidia.com/index.html#x-c-c-cu-x)`--x`

{`c`

|`c++`

|`cu`

} (`-x`

)[4.2.3.28.](https://docs.nvidia.com/index.html#std-c-03-c-11-c-14-c-17-c-20-c-23-std)`--std`

{`c++03`

|`c++11`

|`c++14`

|`c++17`

|`c++20`

|`c++23`

} (`-std`

)[4.2.3.29.](https://docs.nvidia.com/index.html#no-host-device-initializer-list-nohdinitlist)`--no-host-device-initializer-list`

(`-nohdinitlist`

)[4.2.3.30.](https://docs.nvidia.com/index.html#expt-relaxed-constexpr-expt-relaxed-constexpr)`--expt-relaxed-constexpr`

(`-expt-relaxed-constexpr`

)[4.2.3.31.](https://docs.nvidia.com/index.html#extended-lambda-extended-lambda)`--extended-lambda`

(`-extended-lambda`

)[4.2.3.32.](https://docs.nvidia.com/index.html#expt-extended-lambda-expt-extended-lambda)`--expt-extended-lambda`

(`-expt-extended-lambda`

)[4.2.3.33.](https://docs.nvidia.com/index.html#machine-64-m)`--machine`

{`64`

} (`-m`

)[4.2.3.34.](https://docs.nvidia.com/index.html#m64-m64)`--m64`

(`-m64`

)[4.2.3.35.](https://docs.nvidia.com/index.html#host-linker-script-use-lcs-gen-lcs-hls)`--host-linker-script`

{`use-lcs`

|`gen-lcs`

} (`-hls`

)[4.2.3.36.](https://docs.nvidia.com/index.html#augment-host-linker-script-aug-hls)`--augment-host-linker-script`

(`-aug-hls`

)[4.2.3.37.](https://docs.nvidia.com/index.html#relocatable-link-r)`--relocatable-link`

(`-r`

)[4.2.3.38.](https://docs.nvidia.com/index.html#frandom-seed-frandom-seed)`--frandom-seed`

(`-frandom-seed`

)

-
[4.2.4. Options for Passing Specific Phase Options](https://docs.nvidia.com/index.html#options-for-passing-specific-phase-options)[4.2.4.1.](https://docs.nvidia.com/index.html#compiler-options-options-xcompiler)`--compiler-options options,...`

(`-Xcompiler`

)[4.2.4.2.](https://docs.nvidia.com/index.html#linker-options-options-xlinker)`--linker-options options,...`

(`-Xlinker`

)[4.2.4.3.](https://docs.nvidia.com/index.html#archive-options-options-xarchive)`--archive-options options,...`

(`-Xarchive`

)[4.2.4.4.](https://docs.nvidia.com/index.html#ptxas-options-options-xptxas)`--ptxas-options options,...`

(`-Xptxas`

)[4.2.4.5.](https://docs.nvidia.com/index.html#nvlink-options-options-xnvlink)`--nvlink-options options,...`

(`-Xnvlink`

)[4.2.4.6.](https://docs.nvidia.com/index.html#nvprune-options-options-xnvprune)`--nvprune-options options,...`

(`-Xnvprune`

)[4.2.4.7.](https://docs.nvidia.com/index.html#tileiras-options-options-xtileiras)`--tileiras-options options,...`

(`-Xtileiras`

)

-
[4.2.5. Options for Guiding the Compiler Driver](https://docs.nvidia.com/index.html#options-for-guiding-the-compiler-driver)[4.2.5.1.](https://docs.nvidia.com/index.html#static-global-template-stub-true-false-static-global-template-stub)`--static-global-template-stub`

{`true`

|`false`

} (`-static-global-template-stub`

)[4.2.5.2.](https://docs.nvidia.com/index.html#device-entity-has-hidden-visibility-true-false-device-entity-has-hidden-visibility)`--device-entity-has-hidden-visibility`

{`true`

|`false`

} (`-device-entity-has-hidden-visibility`

)[4.2.5.3.](https://docs.nvidia.com/index.html#forward-unknown-to-host-compiler-forward-unknown-to-host-compiler)`--forward-unknown-to-host-compiler`

(`-forward-unknown-to-host-compiler`

)[4.2.5.4.](https://docs.nvidia.com/index.html#forward-unknown-to-host-linker-forward-unknown-to-host-linker)`--forward-unknown-to-host-linker`

(`-forward-unknown-to-host-linker`

)[4.2.5.5.](https://docs.nvidia.com/index.html#forward-unknown-opts-forward-unknown-opts)`--forward-unknown-opts`

(`-forward-unknown-opts`

)[4.2.5.6.](https://docs.nvidia.com/index.html#forward-slash-prefix-opts-forward-slash-prefix-opts)`--forward-slash-prefix-opts`

(`-forward-slash-prefix-opts`

)[4.2.5.7.](https://docs.nvidia.com/index.html#dont-use-profile-noprof)`--dont-use-profile`

(`-noprof`

)[4.2.5.8.](https://docs.nvidia.com/index.html#threads-number-t)`--threads number`

(`-t`

)[4.2.5.9.](https://docs.nvidia.com/index.html#dryrun-dryrun)`--dryrun`

(`-dryrun`

)[4.2.5.10.](https://docs.nvidia.com/index.html#verbose-v)`--verbose`

(`-v`

)[4.2.5.11.](https://docs.nvidia.com/index.html#keep-keep)`--keep`

(`-keep`

)[4.2.5.12.](https://docs.nvidia.com/index.html#keep-dir-directory-keep-dir)`--keep-dir directory`

(`-keep-dir`

)[4.2.5.13.](https://docs.nvidia.com/index.html#save-temps-save-temps)`--save-temps`

(`-save-temps`

)[4.2.5.14.](https://docs.nvidia.com/index.html#clean-targets-clean)`--clean-targets`

(`-clean`

)[4.2.5.15.](https://docs.nvidia.com/index.html#run-args-arguments-run-args)`--run-args arguments,...`

(`-run-args`

)[4.2.5.16.](https://docs.nvidia.com/index.html#use-local-env-use-local-env)`--use-local-env`

(`-use-local-env`

)[4.2.5.17.](https://docs.nvidia.com/index.html#force-cl-env-setup-force-cl-env-setup)`--force-cl-env-setup`

(`-force-cl-env-setup`

)[4.2.5.18.](https://docs.nvidia.com/index.html#input-drive-prefix-prefix-idp)`--input-drive-prefix prefix`

(`-idp`

)[4.2.5.19.](https://docs.nvidia.com/index.html#dependency-drive-prefix-prefix-ddp)`--dependency-drive-prefix prefix`

(`-ddp`

)[4.2.5.20.](https://docs.nvidia.com/index.html#drive-prefix-prefix-dp)`--drive-prefix prefix`

(`-dp`

)[4.2.5.21.](https://docs.nvidia.com/index.html#dependency-target-name-target-mt)`--dependency-target-name target`

(`-MT`

)[4.2.5.22.](https://docs.nvidia.com/index.html#no-align-double)`--no-align-double`

[4.2.5.23.](https://docs.nvidia.com/index.html#no-device-link-nodlink)`--no-device-link`

(`-nodlink`

)[4.2.5.24.](https://docs.nvidia.com/index.html#prune-prune)`--prune`

(`-prune`

)[4.2.5.25.](https://docs.nvidia.com/index.html#options-for-guiding-compiler-driver-allow-unsupported-compiler)`--allow-unsupported-compiler`

(`-allow-unsupported-compiler`

)

-
[4.2.6. Options for Steering CUDA Compilation](https://docs.nvidia.com/index.html#options-for-steering-cuda-compilation) -
[4.2.7. Options for Steering GPU Code Generation](https://docs.nvidia.com/index.html#options-for-steering-gpu-code-generation)[4.2.7.1.](https://docs.nvidia.com/index.html#gpu-architecture-arch)`--gpu-architecture`

(`-arch`

)[4.2.7.2.](https://docs.nvidia.com/index.html#gpu-code-code-code)`--gpu-code code,...`

(`-code`

)[4.2.7.3.](https://docs.nvidia.com/index.html#generate-code-specification-gencode)`--generate-code specification`

(`-gencode`

)[4.2.7.4.](https://docs.nvidia.com/index.html#relocatable-device-code-true-false-rdc)`--relocatable-device-code`

{`true`

|`false`

} (`-rdc`

)[4.2.7.5.](https://docs.nvidia.com/index.html#entries-entry-e)`--entries entry,...`

(`-e`

)[4.2.7.6.](https://docs.nvidia.com/index.html#maxrregcount-amount-maxrregcount)`--maxrregcount amount`

(`-maxrregcount`

)[4.2.7.7.](https://docs.nvidia.com/index.html#use-fast-math-use-fast-math)`--use_fast_math`

(`-use_fast_math`

)[4.2.7.8.](https://docs.nvidia.com/index.html#ftz-true-false-ftz)`--ftz`

{`true`

|`false`

} (`-ftz`

)[4.2.7.9.](https://docs.nvidia.com/index.html#prec-div-true-false-prec-div)`--prec-div`

{`true`

|`false`

} (`-prec-div`

)[4.2.7.10.](https://docs.nvidia.com/index.html#prec-sqrt-true-false-prec-sqrt)`--prec-sqrt`

{`true`

|`false`

} (`-prec-sqrt`

)[4.2.7.11.](https://docs.nvidia.com/index.html#fmad-true-false-fmad)`--fmad`

{`true`

|`false`

} (`-fmad`

)[4.2.7.12.](https://docs.nvidia.com/index.html#extra-device-vectorization-extra-device-vectorization)`--extra-device-vectorization`

(`-extra-device-vectorization`

)[4.2.7.13.](https://docs.nvidia.com/index.html#compile-as-tools-patch-astoolspatch)`--compile-as-tools-patch`

(`-astoolspatch`

)[4.2.7.14.](https://docs.nvidia.com/index.html#keep-device-functions-keep-device-functions)`--keep-device-functions`

(`-keep-device-functions`

)[4.2.7.15.](https://docs.nvidia.com/index.html#jump-table-density-percentage-jtd)`--jump-table-density percentage`

(`-jtd`

)

-
[4.2.8. Generic Tool Options](https://docs.nvidia.com/index.html#generic-tool-options)[4.2.8.1.](https://docs.nvidia.com/index.html#disable-warnings-w)`--disable-warnings`

(`-w`

)[4.2.8.2.](https://docs.nvidia.com/index.html#source-in-ptx-src-in-ptx)`--source-in-ptx`

(`-src-in-ptx`

)[4.2.8.3.](https://docs.nvidia.com/index.html#restrict-restrict)`--restrict`

(`-restrict`

)[4.2.8.4.](https://docs.nvidia.com/index.html#wno-deprecated-gpu-targets-wno-deprecated-gpu-targets)`--Wno-deprecated-gpu-targets`

(`-Wno-deprecated-gpu-targets`

)[4.2.8.5.](https://docs.nvidia.com/index.html#wno-deprecated-declarations-wno-deprecated-declarations)`--Wno-deprecated-declarations`

(`-Wno-deprecated-declarations`

)[4.2.8.6.](https://docs.nvidia.com/index.html#wreorder-wreorder)`--Wreorder`

(`-Wreorder`

)[4.2.8.7.](https://docs.nvidia.com/index.html#fmax-errors-number-fmax-errors)`--fmax-errors=<number>`

(`-fmax-errors`

)[4.2.8.8.](https://docs.nvidia.com/index.html#wdefault-stream-launch-wdefault-stream-launch)`--Wdefault-stream-launch`

(`-Wdefault-stream-launch`

)[4.2.8.9.](https://docs.nvidia.com/index.html#wmissing-launch-bounds-wmissing-launch-bounds)`--Wmissing-launch-bounds`

(`-Wmissing-launch-bounds`

)[4.2.8.10.](https://docs.nvidia.com/index.html#wext-lambda-captures-this-wext-lambda-captures-this)`--Wext-lambda-captures-this`

(`-Wext-lambda-captures-this`

)[4.2.8.11.](https://docs.nvidia.com/index.html#wconversion-wconversion)`--Wconversion`

(`-Wconversion`

)[4.2.8.12.](https://docs.nvidia.com/index.html#werror-kind-werror)`--Werror kind,...`

(`-Werror`

)[4.2.8.13.](https://docs.nvidia.com/index.html#display-error-number-err-no)`--display-error-number`

(`-err-no`

)[4.2.8.14.](https://docs.nvidia.com/index.html#no-display-error-number-no-err-no)`--no-display-error-number`

(`-no-err-no`

)[4.2.8.15.](https://docs.nvidia.com/index.html#diag-error-errnum-diag-error)`--diag-error errNum,...`

(`-diag-error`

)[4.2.8.16.](https://docs.nvidia.com/index.html#diag-suppress-errnum-diag-suppress)`--diag-suppress errNum,...`

(`-diag-suppress`

)[4.2.8.17.](https://docs.nvidia.com/index.html#diag-warn-errnum-diag-warn)`--diag-warn errNum,...`

(`-diag-warn`

)[4.2.8.18.](https://docs.nvidia.com/index.html#resource-usage-res-usage)`--resource-usage`

(`-res-usage`

)[4.2.8.19.](https://docs.nvidia.com/index.html#device-stack-protector-true-false-device-stack-protector)`--device-stack-protector`

{`true`

|`false`

} (`-device-stack-protector`

)[4.2.8.20.](https://docs.nvidia.com/index.html#utf-8-utf-8)`--utf-8`

(`-utf-8`

)[4.2.8.21.](https://docs.nvidia.com/index.html#help-h)`--help`

(`-h`

)[4.2.8.22.](https://docs.nvidia.com/index.html#version-v)`--version`

(`-V`

)[4.2.8.23.](https://docs.nvidia.com/index.html#options-file-file-optf)`--options-file file,...`

(`-optf`

)[4.2.8.24.](https://docs.nvidia.com/index.html#time-filename-time)`--time filename`

(`-time`

)[4.2.8.25.](https://docs.nvidia.com/index.html#qpp-config-config-qpp-config)`--qpp-config config`

(`-qpp-config`

)[4.2.8.26.](https://docs.nvidia.com/index.html#list-gpu-code-code-ls)`--list-gpu-code`

(`-code-ls`

)[4.2.8.27.](https://docs.nvidia.com/index.html#list-gpu-arch-arch-ls)`--list-gpu-arch`

(`-arch-ls`

)[4.2.8.28.](https://docs.nvidia.com/index.html#fdevice-time-trace-fdevice-time-trace)`--fdevice-time-trace`

(`-fdevice-time-trace`

)[4.2.8.29.](https://docs.nvidia.com/index.html#fdevice-sanitize-fdevice-sanitize)`--fdevice-sanitize`

(`-fdevice-sanitize`

)

-
[4.2.9. Phase Options](https://docs.nvidia.com/index.html#phase-options)-
[4.2.9.1. Ptxas Options](https://docs.nvidia.com/index.html#ptxas-options)[4.2.9.1.1.](https://docs.nvidia.com/index.html#allow-expensive-optimizations-allow-expensive-optimizations)`--allow-expensive-optimizations`

(`-allow-expensive-optimizations`

)[4.2.9.1.2.](https://docs.nvidia.com/index.html#ptxas-options-apply-controls)`--apply-controls`

(`-apply-controls`

)[4.2.9.1.3.](https://docs.nvidia.com/index.html#compile-only-c)`--compile-only`

(`-c`

)[4.2.9.1.4.](https://docs.nvidia.com/index.html#compiler-annotations-annotate)`--compiler-annotations`

(`-annotate`

)[4.2.9.1.5.](https://docs.nvidia.com/index.html#def-load-cache-dlcm)`--def-load-cache`

(`-dlcm`

)[4.2.9.1.6.](https://docs.nvidia.com/index.html#def-store-cache-dscm)`--def-store-cache`

(`-dscm`

)[4.2.9.1.7.](https://docs.nvidia.com/index.html#ptxas-options-device-debug)`--device-debug`

(`-g`

)[4.2.9.1.8.](https://docs.nvidia.com/index.html#disable-optimizer-constants-disable-optimizer-consts)`--disable-optimizer-constants`

(`-disable-optimizer-consts`

)[4.2.9.1.9.](https://docs.nvidia.com/index.html#entry-entry-e)`--entry entry,...`

(`-e`

)[4.2.9.1.10.](https://docs.nvidia.com/index.html#fmad-fmad)`--fmad`

(`-fmad`

)[4.2.9.1.11.](https://docs.nvidia.com/index.html#force-load-cache-flcm)`--force-load-cache`

(`-flcm`

)[4.2.9.1.12.](https://docs.nvidia.com/index.html#force-store-cache-fscm)`--force-store-cache`

(`-fscm`

)[4.2.9.1.13.](https://docs.nvidia.com/index.html#ptxas-options-generate-line-info)`--generate-line-info`

(`-lineinfo`

)[4.2.9.1.14.](https://docs.nvidia.com/index.html#gpu-name-gpuname-arch)`--gpu-name gpuname`

(`-arch`

)[4.2.9.1.15.](https://docs.nvidia.com/index.html#ptxas-options-help)`--help`

(`-h`

)[4.2.9.1.16.](https://docs.nvidia.com/index.html#machine-m)`--machine`

(`-m`

)[4.2.9.1.17.](https://docs.nvidia.com/index.html#ptxas-options-maxrregcount)`--maxrregcount amount`

(`-maxrregcount`

)[4.2.9.1.18.](https://docs.nvidia.com/index.html#opt-level-n-o)`--opt-level N`

(`-O`

)[4.2.9.1.19.](https://docs.nvidia.com/index.html#ptxas-options-options-file)`--options-file file,...`

(`-optf`

)[4.2.9.1.20.](https://docs.nvidia.com/index.html#position-independent-code-pic)`--position-independent-code`

(`-pic`

)[4.2.9.1.21.](https://docs.nvidia.com/index.html#preserve-relocs-preserve-relocs)`--preserve-relocs`

(`-preserve-relocs`

)[4.2.9.1.22.](https://docs.nvidia.com/index.html#sp-bounds-check-sp-bounds-check)`--sp-bounds-check`

(`-sp-bounds-check`

)[4.2.9.1.23.](https://docs.nvidia.com/index.html#suppress-async-bulk-multicast-advisory-warning-suppress-async-bulk-multicast-advisory-warning)`--suppress-async-bulk-multicast-advisory-warning`

(`-suppress-async-bulk-multicast-advisory-warning`

)[4.2.9.1.24.](https://docs.nvidia.com/index.html#suppress-sparse-mma-advisory-info-suppress-sparse-mma-advisory-info)`--suppress-sparse-mma-advisory-info`

(`-suppress-sparse-mma-advisory-info`

)[4.2.9.1.25.](https://docs.nvidia.com/index.html#ptxas-options-verbose)`--verbose`

(`-v`

)[4.2.9.1.26.](https://docs.nvidia.com/index.html#ptxas-options-version)`--version`

(`-V`

)[4.2.9.1.27.](https://docs.nvidia.com/index.html#warning-as-error-werror)`--warning-as-error`

(`-Werror`

)[4.2.9.1.28.](https://docs.nvidia.com/index.html#warn-on-double-precision-use-warn-double-usage)`--warn-on-double-precision-use`

(`-warn-double-usage`

)[4.2.9.1.29.](https://docs.nvidia.com/index.html#warn-on-local-memory-usage-warn-lmem-usage)`--warn-on-local-memory-usage`

(`-warn-lmem-usage`

)[4.2.9.1.30.](https://docs.nvidia.com/index.html#warn-on-spills-warn-spills)`--warn-on-spills`

(`-warn-spills`

)[4.2.9.1.31.](https://docs.nvidia.com/index.html#ptxas-options-compile-as-tools-patch)`--compile-as-tools-patch`

(`-astoolspatch`

)[4.2.9.1.32.](https://docs.nvidia.com/index.html#maxntid-maxntid)`--maxntid`

(`-maxntid`

)[4.2.9.1.33.](https://docs.nvidia.com/index.html#minnctapersm-minnctapersm)`--minnctapersm`

(`-minnctapersm`

)[4.2.9.1.34.](https://docs.nvidia.com/index.html#override-directive-values-override-directive-values)`--override-directive-values`

(`-override-directive-values`

)[4.2.9.1.35.](https://docs.nvidia.com/index.html#make-errors-visible-at-exit-make-errors-visible-at-exit)`--make-errors-visible-at-exit`

(`-make-errors-visible-at-exit`

)[4.2.9.1.36.](https://docs.nvidia.com/index.html#ptxas-options-ofast-compile)`--Ofast-compile level`

(`-Ofc`

)[4.2.9.1.37.](https://docs.nvidia.com/index.html#device-stack-protector-device-stack-protector)`--device-stack-protector`

(`-device-stack-protector`

)[4.2.9.1.38.](https://docs.nvidia.com/index.html#g-tensor-memory-access-check-g-tmem-access-check)`--g-tensor-memory-access-check`

(`-g-tmem-access-check`

)[4.2.9.1.39.](https://docs.nvidia.com/index.html#gno-tensor-memory-access-check-gno-tmem-access-check)`--gno-tensor-memory-access-check`

(`-gno-tmem-access-check`

)[4.2.9.1.40.](https://docs.nvidia.com/index.html#split-compile-split-compile)`--split-compile`

(`-split-compile`

)[4.2.9.1.41.](https://docs.nvidia.com/index.html#ptxas-options-jobserver)`--jobserver`

(`-jobserver`

)

[4.2.9.2.](https://docs.nvidia.com/index.html#sanitize-sanitize)`--sanitize`

(`-sanitize`

)-
[4.2.9.3. NVLINK Options](https://docs.nvidia.com/index.html#nvlink-options)[4.2.9.3.1.](https://docs.nvidia.com/index.html#nvlink-options-disable-warnings)`--disable-warnings`

(`-w`

)[4.2.9.3.2.](https://docs.nvidia.com/index.html#nvlink-options-preserve-relocs)`--preserve-relocs`

(`-preserve-relocs`

)[4.2.9.3.3.](https://docs.nvidia.com/index.html#nvlink-options-verbose)`--verbose`

(`-v`

)[4.2.9.3.4.](https://docs.nvidia.com/index.html#nvlink-options-warning-as-error)`--warning-as-error`

(`-Werror`

)[4.2.9.3.5.](https://docs.nvidia.com/index.html#suppress-arch-warning-suppress-arch-warning)`--suppress-arch-warning`

(`-suppress-arch-warning`

)[4.2.9.3.6.](https://docs.nvidia.com/index.html#suppress-stack-size-warning-suppress-stack-size-warning)`--suppress-stack-size-warning`

(`-suppress-stack-size-warning`

)[4.2.9.3.7.](https://docs.nvidia.com/index.html#dump-callgraph-dump-callgraph)`--dump-callgraph`

(`-dump-callgraph`

)[4.2.9.3.8.](https://docs.nvidia.com/index.html#dump-callgraph-no-demangle-dump-callgraph-no-demangle)`--dump-callgraph-no-demangle`

(`-dump-callgraph-no-demangle`

)[4.2.9.3.9.](https://docs.nvidia.com/index.html#xptxas-xptxas)`--Xptxas`

(`-Xptxas`

)[4.2.9.3.10.](https://docs.nvidia.com/index.html#cpu-arch-cpu-arch)`--cpu-arch`

(`-cpu-arch`

)[4.2.9.3.11.](https://docs.nvidia.com/index.html#extra-warnings-extrawarn)`--extra-warnings`

(`-extrawarn`

)[4.2.9.3.12.](https://docs.nvidia.com/index.html#gen-host-linker-script-ghls)`--gen-host-linker-script`

(`-ghls`

)[4.2.9.3.13.](https://docs.nvidia.com/index.html#ignore-host-info-ignore-host-info)`--ignore-host-info`

(`-ignore-host-info`

)[4.2.9.3.14.](https://docs.nvidia.com/index.html#keep-system-libraries-keep-system-libraries)`--keep-system-libraries`

(`-keep-system-libraries`

)[4.2.9.3.15.](https://docs.nvidia.com/index.html#kernels-used-kernels-used)`--kernels-used`

(`-kernels-used`

)[4.2.9.3.16.](https://docs.nvidia.com/index.html#options-file-optf)`--options-file`

(`-optf`

)[4.2.9.3.17.](https://docs.nvidia.com/index.html#report-arch-report-arch)`--report-arch`

(`-report-arch`

)[4.2.9.3.18.](https://docs.nvidia.com/index.html#suppress-debug-info-suppress-debug-info)`--suppress-debug-info`

(`-suppress-debug-info`

)[4.2.9.3.19.](https://docs.nvidia.com/index.html#variables-used-variables-used)`--variables-used`

(`-variables used`

)[4.2.9.3.20.](https://docs.nvidia.com/index.html#nvlink-options-device-stack-protector)`--device-stack-protector`

{`true`

|`false`

} (`-device-stack-protector`

)


-

-
[4.3. NVCC Environment Variables](https://docs.nvidia.com/index.html#nvcc-environment-variables)

-
[5. GPU Compilation](https://docs.nvidia.com/index.html#gpu-compilation) -
[6. Using Separate Compilation in CUDA](https://docs.nvidia.com/index.html#using-separate-compilation-in-cuda) [7. Tile Compilation in CUDA](https://docs.nvidia.com/index.html#tile-compilation-in-cuda)-
[8. Miscellaneous NVCC Usage](https://docs.nvidia.com/index.html#miscellaneous-nvcc-usage) -
[9. Notices](https://docs.nvidia.com/index.html#notices)