source: https://github.com/security/advanced-security/secret-protection?locale=de-de

# Geheimhaltung von Geheimnissen

GitHub Secret Protection überwacht kontinuierlich deinen GitHub Perimeter und trägt dazu bei, Offenlegungen zu vermeiden, Zugangsdaten zu schützen und Software sicher zu veröffentlichen.

4,4 Mio. Geheimnisse wurden 2024 auf GitHub vor Offenlegung geschützt.

Über 150 Branchenpartner arbeiten zur Risikominimierung für die Entwickler‑Community zusammen.

39 Mio. erkannte Secret‑Leaks mit Secret Protection (2024)

## Verhindere, dass Geheimnisse in deinen Repositorys versehentlich veröffentlicht werden

Durch den Push-Schutz werden Geheimnisse automatisch blockiert, bevor sie in dein Repository gelangen. So bleibt der Code sauber, ohne dass Workflows gestört werden.

Mit Secret Scanning kannst du Geheimnisse u. a. in Issues und Diskussionen erkennen. Metadaten wie Gültigkeitsprüfungen und öffentliche Leaks tragen dazu bei, aktive Bedrohungen zu priorisieren.

Erkennung schwer auffindbarer Secrets, einschließlich Passwörtern, ohne Fehlalarme. Secrets, die von herkömmlichen Secret‑Detektoren nicht erfasst werden, können erkannt werden – für eine zusätzliche Sicherheitsebene.

Bewerte mit unserem kostenlosen Tool zur Risikobewertung, inwieweit deine Codebasis durch Anwendungsschwachstellen und offengelegte Geheimnisse gefährdet ist.

[Mehr zu den GitHub Security-Sicherheitsrisikobewertungen](https://github.com/security/advanced-security/assessments?locale=de-DE)

### GitHub arbeitet mit über 150 Anbietern zusammen, um Risiken zu minimieren und bei der Erkennung ein Höchstmaß an Genauigkeit zu gewährleisten.

[Weitere Informationen zum Partnerprogramm für Secret Scanning](https://docs.github.com/code-security/secret-scanning/secret-scanning-partnership-program/secret-scanning-partner-program)

### Sichererer Code für alle

Ganz gleich, ob du ein Open-Source-Projekt sichern oder die Codebasis des Unternehmens stärken möchtest: GitHub Secret Protection hilft dir, Geheimnisse aus deinem Code herauszuhalten.

[Demo anfordern](https://www.github.com/security/advanced-security/demo?utm_campaign=Demo_utmroutercampaign&ref_cta=Request%20demo&ref_loc=footer&ref_page=%2Fsecret_protection_lp)

[Pakete und Preise](http://github.com/security/plans?ref_cta=pricing&ref_loc=footer&ref_page=%2Fsecret_protection_lp&locale=de-DE)

## Ressourcen für den Einstieg

[Entwicklungsorientierte Anwendungssicherheit entdecken](https://resources.github.com/security/mission-copilot-autofix-securing-the-worlds-software/)

Verschaffe dir einen umfassenden Überblick über den aktuellen Stand beim Thema Anwendungssicherheit.

[Leitfaden zu DevSecOps erkunden](https://github.com/resources/whitepapers/the-enterprise-guide-to-ai-powered-devsecops?locale=de-DE)

Erfahre, wie du deinen Code mit DevSecOps von Anfang an sicher gestalten kannst.

[Fehlerquellen bei der Anwendungssicherheit vermeiden](https://github.com/resources/whitepapers/three-appsec-pitfalls-security?locale=de-DE)

Lerne häufige Fehlerquellen bei der Anwendungssicherheit kennen und erfahre, wie sie sich vermeiden lassen.

### Häufig gestellte Fragen

#### Wozu dient GitHub Secret Protection?


GitHub Secret Protection erkennt und verhindert Geheimnis-Leaks kontinuierlich und in Echtzeit. Durch den Push-Schutz wird proaktiv verhindert, dass sensible Zugangsdaten per Push in ein Repository übertragen werden. Dank einer bemerkenswert niedrigen Rate falsch positiver Ergebnisse und rund 150 Integrationen von Dienstanbietern ermöglicht es die schnelle Entziehung und Rotation von Zugangsdaten. Dadurch wird die Produktivität der Entwickler:innen gesteigert.

#### Wozu dient die Risikobewertung für Geheimnisse?


Die Risikobewertung für Geheimnisse bietet einen kostenlosen, umfassenden Überblick darüber, wie viele Geheimnisse in den GitHub Repositorys einer Organisation insgesamt offengelegt wurden. Durch die Analyse der Repositorys auf offengelegte Geheimnisse hin hilft sie Administrator:innen und Entwickler:innen, potenzielle Sicherheitsrisiken nachzuvollziehen. Außerdem liefert sie umsetzbare Erkenntnisse für Abhilfemaßnahmen. Weitere Informationen zu den GitHub Security-Sicherheitsrisikobewertungen.

#### Wozu dient der Push-Schutz?


Der Push-Schutz soll von vornherein verhindern, dass sensible Informationen wie Geheimnisse oder Token per Push in dein Repository übertragen werden. Dazu wird dein Code während des Push-Vorgangs proaktiv nach Geheimnissen durchsucht. Werden welche gefunden, wird der Push-Vorgang blockiert.

#### Wozu dient die delegierte Umgehung für den Push-Schutz?


Die delegierte Umgehung führt einen Genehmigungsprozess ein, über den Entwickler:innen den Push-Schutz umgehen können. Wer eine Sperre durch den Push-Schutz umgehen möchte, muss eine entsprechende Anfrage an eine festgelegte Gruppe von Prüfenden übermitteln. So wird gewährleistet, dass keine risikobehafteten Geheimnisse versehentlich offengelegt werden.

#### Wozu dienen Gültigkeitsprüfungen für Geheimnisse?


Anhand von Gültigkeitsprüfungen kannst du feststellen, ob erkannte Geheimnisse noch aktiv sind. So können Entwickler:innen und Sicherheitsteams ihre Maßnahmen effektiv priorisieren. Bei Kennzeichnung eines Geheimnisses überprüft das System dessen Gültigkeit, um festzustellen, ob es aktiv oder inaktiv ist.

#### Wozu dient das Partnerschaftsprogramm für Secret Scanning?


Dank des Partnerschaftsprogramms für Secret Scanning können Dienstanbieter ihre Token-Formate sichern. Dazu durchsucht GitHub öffentliche Repositorys und npm-Pakete nach offengelegten Geheimnissen. Wird ein Geheimnis in einem öffentlichen Repository gefunden, sendet GitHub eine Warnung direkt an den Dienstanbieter. Dieser kann dann eine Prüfung durchführen und entsprechende Maßnahmen ergreifen.