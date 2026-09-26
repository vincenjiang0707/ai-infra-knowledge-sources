source: https://github.com/features/code-quality?locale=fr-fr

L’analyse déterministe de CodeQL détecte ce que les règles savent traiter. La détection assistée par IA repère ce qui leur échappe. Ensemble, elles suivent le rythme d’un code que les équipes de développement génèrent plus vite qu’aucune bibliothèque de règles ne peut évoluer.

# GitHub Code Quality

GitHub Code Quality affiche les problèmes détectés dans les pull requests avec des correctifs révisables avant le merge, puis vous aide à appliquer des normes cohérentes grâce aux ensembles de règles.

## Restez dans le workflow

GitHub Code Quality affiche les problèmes détectés directement dans les pull requests, évitant ainsi aux développeurs de devoir passer par un tableau de bord distinct.

### Corrigez les problèmes à mesure que vous révisez

Chaque problème identifié inclut un correctif révisable que les développeurs peuvent appliquer avant le merge.

### Réduisez le backlog et livrez plus vite

Consacrez moins de temps à trier les problèmes de qualité et davantage à examiner et livrer des correctifs.

## Tout ce qu’il faut pour garantir la qualité

### Corriger à la source

Vos équipes de développement n’ouvrent pas de tableau de bord. Elles ouvrent une pull request. Copilot Autofix suggère le correctif sur place. Elles l’examinent, le modifient ou l’ignorent. Rien ne merge tout seul.

### Une norme unique, peu importe qui (ou quoi) écrit le code

Les mêmes ensembles de règles encadrent le code écrit par les équipes de développement, les résultats renvoyés par la revue de code Copilot et les pull requests ouvertes par les agents de codage. Qualité et sécurité, un seul workflow.

## Adoptez Code Quality dans votre organisation

La qualité dans la pull request, la gouvernance à l’échelle de l’organisation.

### Code Quality

La qualité dans la pull request, la gouvernance à l’échelle de l’organisation.

$10USDpar committer / mois + utilisation

#### Ce qui est inclus


- Détection hybride (CodeQL déterministe et détection assistée par IA)
- Autofix dans la pull request
- Contrôles qualité des ensembles de règles, seuils de couverture et protection au moment du merge
- Notation de la maintenabilité et de la fiabilité
- Ingestion de la couverture (Cobertura XML)
- Déploiement à l’échelle de l’organisation, tableaux de bord et API

10 USD par committer / mois, plus une facturation à l’usage pour les fonctionnalités d’IA et les minutes Actions. Référentiels publics : 0 USD par committer + facturation à l’usage pour les tâches alimentées par l’IA. Disponible sur GitHub Enterprise Cloud et GitHub Team.

### Questions fréquentes

#### Combien coûte Code Quality ?


10 USD par committer et par mois, plus une facturation à l’usage pour les tâches alimentées par l’IA. Les analyses déterministes CodeQL consomment des minutes GitHub Actions. Les référentiel publics n’entraînent aucun coût par committer, avec une facturation à l’usage pour les fonctionnalités alimentées par l’IA.

#### Quels langages Code Quality prend-il en charge ?


Java, JavaScript, TypeScript, Python, Ruby, C# et Go.

#### Ai-je besoin d’un autre outil pour la couverture de test ?


Non. Code Quality génère des rapports de couverture à partir de vos outils de test existants au format Cobertura XML, puis conditionne les merges au respect de vos seuils grâce aux ensembles de règles. L’outil lit votre couverture ; il n’instrumente pas vos tests.

#### En quoi est-ce différent de GitHub Advanced Security ?


GitHub Advanced Security couvre la sécurité : Code Security détecte les vulnérabilités, et Secret Protection détecte les identifiants exposés. Code Quality couvre la maintenabilité, la fiabilité et la couverture, et ces deux disciplines fonctionnent ensemble. Les problèmes de qualité sont souvent à l’origine des vulnérabilités : un code plus propre allège donc la charge de travail des équipes de sécurité. Code Quality et Code Security s’appuient sur le même moteur CodeQL, et les deux s’affichent dans une vue d’ensemble unique de la sécurité et de la qualité.

#### Code Quality fonctionne-t-il avec la revue de code Copilot ?


Oui, sous la forme d’expériences intégrées mais distinctes. La revue de code Copilot donne aux équipes de développement des retours contextuels pendant qu’elles rédigent le code, et ses commentaires sont éphémères. Code Quality fournit aux équipes de direction des résultats persistants, des contrôles applicables et des rapports couvrant l’ensemble des repos et des périodes. Les deux apparaissent dans la pull request.

#### Code Quality est-il un produit de conformité ?


Non. Code Quality prend en charge la gouvernance interne et le workflow de développeur. Il ne constitue pas une attestation de conformité à une norme réglementaire ou à un framework d’audit.

#### Puis-je piloter la qualité à l’échelle de toute mon organisation ?


Oui. Déployez Code Quality à l’échelle de l’organisation grâce aux tableaux de bord, aux actions groupées, aux API ainsi qu’à la notation au niveau des repos et de l’organisation.

#### Où mon équipe peut-elle apprendre à le configurer ?


Le parcours d’apprentissage GitHub Code Quality explique comment activer les vérifications, configurer les ensembles de règles, corriger les résultats avec Autofix et lire les tableaux de bord. [Lancer le parcours](https://learn.github.com/learning-pathways/github-code-quality).