source: https://rocm.docs.amd.com/en/latest/about/license.html

# ROCm licenses[#](https://rocm.docs.amd.com#rocm-licenses)

MIT License

Copyright © 2023 - 2026 Advanced Micro Devices, Inc. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Note

The preceding license applies to the [ROCm repository](https://github.com/ROCm/ROCm), which
primarily contains documentation. For licenses related to other ROCm components, refer to the
following section.

## ROCm component licenses[#](https://rocm.docs.amd.com#rocm-component-licenses)

ROCm is released by Advanced Micro Devices, Inc. (AMD) and is licensed per component separately. The following table is a list of ROCm components with links to their respective license terms. These components may include third party components subject to additional licenses. Please review individual repositories for more information.

Component |
License |
|---|---|

Open sourced ROCm components are released via public GitHub
repositories, packages on [https://repo.radeon.com](https://repo.radeon.com) and other distribution channels.
Proprietary products are only available on [https://repo.radeon.com](https://repo.radeon.com).
Proprietary components are organized in a proprietary subdirectory in the package
repositories to distinguish from open sourced packages.

Note

The following additional terms and conditions apply to your use of ROCm technical documentation.

©2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.

The information presented in this document is for informational purposes only and may contain technical inaccuracies, omissions, and typographical errors. The information contained herein is subject to change and may be rendered inaccurate for many reasons, including but not limited to product and roadmap changes, component and motherboard version changes, new model and/or product releases, product differences between differing manufacturers, software changes, BIOS flashes, firmware upgrades, or the like. Any computer system has risks of security vulnerabilities that cannot be completely prevented or mitigated. AMD assumes no obligation to update or otherwise correct or revise this information. However, AMD reserves the right to revise this information and to make changes from time to time to the content hereof without obligation of AMD to notify any person of such revisions or changes.

THIS INFORMATION IS PROVIDED “AS IS.” AMD MAKES NO REPRESENTATIONS OR WARRANTIES WITH RESPECT TO THE CONTENTS HEREOF AND ASSUMES NO RESPONSIBILITY FOR ANY INACCURACIES, ERRORS, OR OMISSIONS THAT MAY APPEAR IN THIS INFORMATION. AMD SPECIFICALLY DISCLAIMS ANY IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR ANY PARTICULAR PURPOSE. IN NO EVENT WILL AMD BE LIABLE TO ANY PERSON FOR ANY RELIANCE, DIRECT, INDIRECT, SPECIAL, OR OTHER CONSEQUENTIAL DAMAGES ARISING FROM THE USE OF ANY INFORMATION CONTAINED HEREIN, EVEN IF AMD IS EXPRESSLY ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

AMD, the AMD Arrow logo, ROCm, and combinations thereof are trademarks of Advanced Micro Devices, Inc. Other product names used in this publication are for identification purposes only and may be trademarks of their respective companies.

### Package licensing[#](https://rocm.docs.amd.com#package-licensing)

Attention

ROCprof Trace Decoder and AOCC CPU optimizations are provided in binary form, subject to the license agreement enclosed on [GitHub](https://github.com/ROCm/rocprof-trace-decoder/blob/amd-mainline/LICENSE) for ROCprof Trace Decoder, and [Developer Central](https://www.amd.com/en/developer/aocc.html) for AOCC. By using, installing,
copying or distributing ROCprof Trace Decoder or AOCC CPU Optimizations, you agree to
the terms and conditions of this license agreement. If you do not agree to the
terms of this agreement, do not install, copy or use ROCprof Trace Decoder or the
AOCC CPU Optimizations.

For the rest of the ROCm packages, you can find the licensing information at the
following location: `/opt/rocm/share/doc/<component-name>/`

or in the locations
specified in the preceding table.

For example, you can fetch the licensing information of the `amd_comgr`

component (Code Object Manager) from the `/opt/rocm/share/doc/amd_comgr/LICENSE.txt`

file.