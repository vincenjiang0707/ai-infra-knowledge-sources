source: https://github.com/features/code-quality?locale=ko-kr

결정론적 CodeQL 분석은 규칙이 처리하는 부분을 포착하고, AI 지원 탐지는 규칙이 놓치는 부분을 포착합니다. 이 둘을 통해 어떤 규칙 라이브러리보다도 빠르게 개발자가 생성하는 코드의 속도를 따라잡을 수 있습니다.

# GitHub Code Quality

## 워크플로 그대로 유지

GitHub Code Quality는 pull request에 바로 결과를 보여주므로 개발자가 별도의 대시보드로 옮겨가지 않아도 됩니다.

### 검토하면서 바로 문제 수정

각 결과에는 개발자가 병합 전 적용할 수 있는 검토 가능한 수정 사항이 포함됩니다.

### 더 적은 백로그, 더 빠른 배포

품질 문제를 분류하는 데 드는 시간을 줄이고 수정 사항을 검토하고 배포하는 데 더 많은 시간을 할애하세요.

## 품질 관리에 필요한 모든 것

### 소스에서 수정

개발자는 대시보드를 열지 않고, pull request를 엽니다. Copilot Autofix가 바로 거기에서 수정 사항을 제안합니다. 개발자는 이를 검토, 편집 또는 무시합니다. 어떤 것도 자동으로 병합되지 않습니다.

### 누가 또는 무엇이 코드를 작성하든 상관없이 하나의 표준 적용

개발자가 작성하는 코드, Copilot 코드 검토에서 반환되는 결과, 코딩 에이전트가 여는 pull request에 모두 동일한 rulesets가 적용됩니다. 품질 및 보안, 하나의 워크플로.

## 조직에 Code Quality 도입

pull request의 품질, 조직 전반의 거버넌스.

### Code Quality

pull request의 품질, 조직 전반의 거버넌스.

$10USD커미터당/월 + 사용량

#### 포함 내용


- 하이브리드 탐지(결정론적 CodeQL 및 AI 지원)
- pull request의 Autofix
- Rulesets 품질 제어, 커버리지 임곗값, 병합 보호
- 유지 관리 기능 및 안정성 평가
- 커버리지 수집(Cobertura XML)
- 조직 전체 배포, 대시보드 및 API

커미터당 월 10달러이며, AI 기능 및 Actions 시간에 대해 사용량에 따라 요금이 부과됩니다. 퍼블릭 리포지토리: 커미터당 0달러이며 AI 기반 작업에 대해 사용량에 따라 요금이 부과됩니다. GitHub Enterprise Cloud와 GitHub Team에서 이용 가능합니다.

### 자주 묻는 질문

#### Code Quality 이용 요금은 얼마인가요?


커미터당 월 10달러이며, AI 기반 작업 사용량에 따라 요금이 부과됩니다. 결정론적 CodeQL 스캔은 GitHub Actions 시간을 사용합니다. 퍼블릭 리포지토리의 경우 커미터당 요금은 없으며, AI 기반 기능에 대해 사용량에 따라 요금이 부과됩니다.

#### Code Quality는 어떤 언어를 지원하나요?


Java, JavaScript, TypeScript, Python, Ruby, C#, Go를 지원합니다.

#### 테스트 커버리지를 위해 다른 도구가 필요한가요?


아니요. Code Quality가 기존 테스트 도구의 커버리지 보고서를 Cobertura XML 형식으로 렌더링한 다음, rulesets를 통해 설정한 임곗값에 따라 병합을 제어합니다. 커버리지를 읽을 뿐 테스트를 계측하지는 않습니다.

#### 이 기능은 GitHub Advanced Security와 어떻게 다른가요?


GitHub Advanced Security는 보안을 다룹니다. Code Security가 취약점을 찾고 Secret Protection이 노출된 자격 증명을 찾습니다. Code Quality는 유지관리성, 안정성, 커버리지를 다루며, 이 두 영역은 서로 연동되어 작동합니다. 품질 문제는 취약점이 숨기 좋은 곳이므로 코드가 깔끔할수록 보안 팀이 추론해야 할 사항이 줄어듭니다. Code Quality와 Code Security는 동일한 CodeQL 엔진에서 실행되며 둘 다 하나의 보안 및 품질 개요를 통해 보고합니다.

#### Code Quality가 Copilot 코드 검토와 연동되나요?


예, 통합되어 있으면서도 별개의 기능으로 작동합니다. Copilot 코드 검토는 개발자가 코드를 작성하는 동안 상황에 맞는 피드백을 제공하며 주석은 사용 후 삭제됩니다. Code Quality는 리더에게 지속적인 결과, 강제 적용 가능한 제어, 여러 리포지토리와 시간에 대한 보고서를 제공합니다. 둘 다 pull request에 표시됩니다.

#### Code Quality는 규정 준수 제품인가요?


아니요. Code Quality는 내부 거버넌스와 개발자 워크플로를 지원합니다. 규제 표준이나 감사 프레임워크에 대한 증명이 아닙니다.

#### 조직 전체의 품질을 관리할 수 있나요?


예. 대시보드, 대량 작업, API, 리포지토리 및 조직 수준의 평가와 함께 조직 전체에 Code Quality를 배포하세요.

#### 어디에서 설정 방법을 확인할 수 있나요?


GitHub Code Quality 학습 경로에서 검사 활성화, rulesets 설정, Autofix를 활용한 결과 수정, 대시보기 읽기 방법을 안내합니다. [학습 경로를 시작하세요](https://learn.github.com/learning-pathways/github-code-quality).