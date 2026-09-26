source: https://github.com/security/advanced-security/secret-protection?locale=ko-kr

# Secret을 비밀로 유지

GitHub Secret Protection은 GitHub 주변을 지속적으로 모니터링하여 노출 방지, 자격 증명 보호 및 안전한 제공을 돕습니다.

440만 2024년 GitHub에서 유출 방지된 secret 수

150+ 개발자 커뮤니티의 위험을 완화하기 위해 협력 중인 업계 파트너 수

3,900만 2024년 Secret Protection으로 감지된 secret 유출 수

## 리포지토리 전체에서 의도치 않은 secret 노출 방지

Push 보호 기능은 기밀 정보가 리포지토리에 도달하기 전에 자동으로 차단하여 워크플로를 방해하지 않고 코드를 안전하게 유지합니다.

Secret scanning으로 GitHub Issues, GitHub Discussions 등에서 secret을 감지하세요. 유효성 검사 및 공개 유출과 같은 메타데이터는 활성 위협의 우선순위를 정하는 데 도움이 됩니다.

GitHub Copilot은 비밀번호처럼 찾기 어려운 secret을 False positives(오탐) 없이 찾아냅니다. 기존의 secret 감지기로는 찾아내기 힘든 secret을 감지하여 보안을 한층 더 강화합니다.

무료 리스크 평가 도구로 코드베이스의 앱 취약성과 유출된 secret에 대한 노출을 평가하세요.

[GitHub 보안 리스크 평가 살펴보기](https://github.com/security/advanced-security/assessments?locale=ko-KR)

### GitHub는 150개 이상의 공급자와 협력하여 위험을 완화하고 최고 수준의 감지 정확도를 보장합니다.

[Secret scanning 파트너 프로그램에 대해 알아보기](https://docs.github.com/code-security/secret-scanning/secret-scanning-partnership-program/secret-scanning-partner-program)

### 모두를 위한 더 안전한 코드

오픈 소스 프로젝트를 보호하든 엔터프라이즈 코드베이스를 강화하든 Secret Protection은 코드에서 secret을 보호하는 데 도움이 됩니다.

[데모 요청](https://www.github.com/security/advanced-security/demo?utm_campaign=Demo_utmroutercampaign&ref_cta=Request%20demo&ref_loc=footer&ref_page=%2Fsecret_protection_lp)

[요금제 및 가격 보기](http://github.com/security/plans?ref_cta=pricing&ref_loc=footer&ref_page=%2Fsecret_protection_lp&locale=ko-KR)

## 초기 시작을 위한 자료

### 자주 묻는 질문

#### GitHub Secret Protection이란 무엇인가요?


GitHub Secret Protection은 실시간으로 secret 유출을 지속적으로 감지하고 방지하며, push 보호를 통해 민감한 자격 증명이 리포지토리로 푸시되는 것을 사전에 차단합니다. 놀랍도록 낮은 False positives(오탐) 비율과 약 150개의 서비스 공급자 통합을 통해 신속한 자격 증명 회수와 교체를 지원하여 개발자 생산성이 향상됩니다.

#### Secret 위험 평가란 무엇인가요?


Secret 위험 평가는 조직의 GitHub 리포지토리 전반에 걸친 secret 유출 현황에 대한 포괄적인 개요를 무료로 제공합니다. 리포지토리에 노출된 secret이 있는지 분석하여 관리자와 개발자가 잠재적 보안 리스크에 대한 노출 정도를 파악할 수 있게 돕고 수정을 위한 실행 가능한 인사이트를 제공합니다. GitHub 보안 리스크 평가에 대해 자세히 알아보세요.

#### Push 보호란 무엇인가요?


Push 보호는 secret이나 토큰과 같은 민감한 정보가 처음부터 리포지토리에 푸시되는 것을 방지하도록 설계되었습니다. Push 프로세스 중 코드 내 secret을 사전에 스캔하고, secret이 감지되면 push를 차단합니다.

#### Push 보호를 위한 위임된 우회란 무엇인가요?


위임된 우회는 개발자가 push 보호를 우회하기 위해 승인 프로세스를 도입합니다. Push 보호 차단을 우회하려는 경우 지정된 위험한 secret이 실수로 유출되지 않도록 검토자 그룹에 요청을 제출해야 합니다.

#### Secret scanning 유효성 검사란 무엇인가요?


유효성 검사를 통해 감지된 secret이 여전히 활성 상태인지 확인할 수 있으며, 이를 통해 개발자와 보안 팀은 효과적으로 대응 우선순위를 정할 수 있습니다. Secret에 플래그가 지정되면 시스템은 해당 secret의 유효성을 검증하여 secret이 활성 상태인지, 비활성 상태인지 확인합니다.

#### Secret scanning 파트너십 프로그램이란 무엇인가요?


Secret scanning 파트너십 프로그램을 통해 서비스 공급자는 GitHub가 퍼블릭 리포지토리와 npm 패키지에서 노출된 secret을 스캔할 수 있도록 하여 토큰 형식을 보호할 수 있습니다. 퍼블릭 리포지토리에서 secret이 발견되면 GitHub에서 서비스 공급자에게 직접 알림을 보냅니다. 그러면 서비스 공급자가 이를 검증하고 적절한 조치를 취할 수 있습니다.