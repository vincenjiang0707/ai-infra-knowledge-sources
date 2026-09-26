source: https://github.com/resources/articles/what-is-cross-site-scripting

# What is Cross-Site Scripting (XSS)

Cross-site scripting (XSS) is a persistent threat to web security. Understanding its types, mechanics, and impact is key to adopting effective prevention strategies.

## What is Cross-site scripting?

Cross-site scripting (XSS) is a type of web [application security](https://github.com/resources/articles/what-is-application-security) vulnerability. XSS allows attackers to inject malicious scripts, most commonly client-side JavaScript, into websites. These malicious scripts are executed by the victim’s web browser when the browser loads the web page. The scripts can be used to steal sensitive data, manipulate website behavior, or even redirect users to malicious sites.

## Overview of cross-site scripting

XSS poses a significant threat because it targets a broad range of users, from individuals to large organizations that rely heavily on web applications.

JavaScript XSS attacks are often used to access sensitive information because JavaScript has access to a visitor’s browser cookies. Attackers can use XSS to use stolen cookies to impersonate the visitor online. Attackers can also use this method to gain access to a user’s webcam data, geolocation information, and other personal information such as bank account numbers.

For larger organizations, cross-site scripting attacks can result in severe consequences, including data breaches, financial loss, and reputational damage. Understanding and mitigating XSS vulnerabilities is essential for maintaining secure web applications.

## Types of cross-site scripting attacks and examples

Cross-site scripting attacks are categorized into three main types: persistent (stored), reflected, and DOM-based XSS. Each type works differently and exploits specific weaknesses in web applications.

### Persistent (stored) XSS

In a persistent XSS attack, malicious scripts are permanently stored on the target server, often in a database or message board. Persistent XSS attacks happen on websites with user-generated content, such as forums or social media sites. When a user visits a page containing these stored scripts, the malicious code is executed in their browser.

**Persistent XSS example: **An attacker posts a malicious script in a blog comment section. When other users view the comment, their browsers execute the script, potentially stealing cookies or personal data.

Persistent XSS attacks are particularly dangerous because they don’t require user interaction beyond simply visiting the compromised resource. This means a single script can affect a large number of users, amplifying its impact.

### Reflected XSS

In contrast to persistent XSS attacks, reflected XSS attacks don’t require the attacker to store the malicious script on the server. Instead, these attacks are carried out by reflecting the user's input back to the user without proper validation.

Reflected XSS typically involves malicious scripts embedded in URLs. The script is executed when victims interact with the crafted link, and the server reflects the attack back to the victim's browser. This is the most common type of cross-site scripting attack and is often used in social engineering or phishing attempts to trick the victim into clicking the malicious link.

**Reflected XSS example: **An attacker sends a legitimate-looking email that appears to be from the user’s bank, directing the user to click a provided link to take a required action on the bank’s website. While the first part of the URL looks legitimate, the attacker has embedded a script in the query string at the end of the URL. When the victim clicks the link, the malicious script executes, stealing sensitive data like session tokens.

### DOM-based XSS

DOM-based cross-site scripting is similar to reflected XSS because it’s delivered through a URL that contains malicious script. However, unlike reflected XSS, DOM-based XSS occurs entirely within the browser’s Document Object Model (DOM)―a system used to represent and work with parts of an HTML document as seen by the browser. When a malicious script runs in the DOM, it can access and change parts of the page, which can lead to unwanted actions or data theft.

DOM-based XSS runs in the user's browser without their knowledge, but the actual webpage sent by the server doesn't change. Since the malicious script is not embedded in the page’s source code, DOM-based XSS often goes undetected by server-side attack detection tools.

**DOM-based XSS example: **A legitimate website may feature a comment section for user interaction. An attacker could exploit this by posting a comment embedded with a script that manipulates the DOM, compromising the data of subsequent visitors.

## How XSS attacks work

XSS attacks occur when a web application makes use of unvalidated or unencoded user input within the output it generates. The attacker can supply a crafted URL, a form that includes malicious code, or a script stored in a database, which is then executed by the victim's browser. This happens in three steps:

**Injection:**The attacker identifies a weakness in the web application, which permits them to insert malicious scripts into the web page. The attacker does this by submitting corrupted data to a form or exploiting a code flaw in the application.**Execution:**When a user visits the compromised web page, their browser executes the malicious script. This is because the browser interprets the script as part of the web page and executes it accordingly.**Exploitation:**Upon execution, the malicious script can engage in a range of actions, including data theft, session hijacking, or redirecting users to sites with nefarious intent.

## Types of XSS attacks

Attackers can use cross-site scripting to steal sensitive information and compromise the security of web applications. Here are some of the most common ways attackers use XSS:

**Cookie theft**: Using XSS, attackers inject scripts that steal session cookies, allowing them to impersonate users and gain unauthorized access.**Session hijacking:**Attackers gain control of user sessions, potentially accessing sensitive data and executing unauthorized actions on the user's behalf.**Keylogging:**Malicious scripts record users' keystrokes, capturing sensitive information such as passwords.**Phishing:**Attackers use XSS to redirect users to fake login pages, capture their credentials, and exploit them for malicious purposes.

For individuals, cross-site scripting attacks can result in identity theft, account hijacking, loss of privacy for their browser history and clipboard contents, and even remote browser control by the attackers. Organizations often suffer financial losses, data leaks, regulatory penalties, and a negative impact on their reputation.

## Preventing cross-site scripting (XSS)

To help mitigate XSS attacks, first detect vulnerabilities through proactive measures like regular [vulnerability scanning](https://github.com/resources/articles/what-is-vulnerability-scanning) and code scanning. Once potential weaknesses are detected, implement strong prevention techniques—such as input validation, output encoding, and secure development practices—to help [safeguard applications](https://github.com/enterprise/advanced-security) from exploitation.

### Detecting XSS vulnerabilities

Regular security assessments, such as vulnerability scanning and static code analysis, help identify potential XSS risks before they can be exploited. Integrate these detection methods into the software development lifecycle to catch vulnerabilities early.

### Using XSS prevention techniques

Adopting effective XSS prevention strategies helps you strengthen security, protect user data, and minimize vulnerabilities.

**Input validation:** Validate and sanitize all user inputs before processing them to prevent malicious scripts from being executed.

Check for potentially malicious characters or scripts and reject any suspicious input or unexpected input formats.

Implement a whitelist approach where only known safe inputs are accepted.


**Output encoding:** Encode all user-generated content before displaying it on the web page. This will help prevent malicious scripts from being executed by the browser.

Encode data before rendering it in a browser to neutralize malicious scripts.

Use context-specific encoding libraries to help ensure secure rendering.


*Code example: Secure output encoding in JavaScript *

*const userInput = "<script>alert('XSS');</script>";
const encodedInput = encodeURIComponent(userInput);
console.log(encodedInput); // Outputs: %3Cscript%3Ealert('XSS')%3C%2Fscript%3E*

**Use of security libraries and frameworks with integrated protection:** Make sure your security libraries and frameworks offer pre-built protection against XSS attacks to automate input validation and output encoding, diminishing the risk of vulnerabilities.

Employ trusted libraries like OWASP’s Java Encoder Project to streamline secure coding.

Use frameworks that include built-in protection against XSS, such as Angular or React.


Beyond input validation and output encoding, embedding security throughout the development process helps you proactively defend against XSS attacks and reduce the risk of exploitation.

## Mitigating cross-site scripting on the client side

In addition to server-side prevention, there are several client-side strategies to mitigate XSS attacks:

**Content security policy (CSP):**CSP is a security feature that allows a website to define a list of trusted sources from which scripts can be loaded. This helps mitigate the risk of cross-site scripting (XSS) attacks by restricting the origins of such scripts.**HTTP-only cookies:**The HttpOnly attribute is used to prevent client-side scripts from accessing cookies. Mark cookies as HTTP-only to reduce the risk of cookie theft.**Browser security features:**Modern browsers are equipped with a range of security features, including XSS filters and clickjacking protection, which can help reduce the impact of XSS attacks. Encourage users to use up-to-date browsers and to activate the built-in security features.

## Real-world examples of XSS attacks

XSS attacks have long been a significant risk to web applications. Real-world cross-site scripting examples show how they can cause serious harm to both individual users and larger organizations:

**Zoom (2020)**: A persistent XSS flaw in Zoom’s web client allowed attackers to inject malicious code via chat. Though quickly patched, the issue added to Zoom’s security concerns, forcing a 90-day feature freeze to focus on security improvements.**WordPress WPBakery Page Builder Plugin (2020)**: A stored XSS flaw in WPBakery’s Page Builder plugin let attackers inject malicious scripts into thousands of WordPress sites. Mass defacements, potential data theft, and emergency patches caused downtime and financial losses, damaging the plugin’s reputation.**Slack (2021)**: A stored XSS vulnerability in Slack’s shared workspace invitations let attackers inject scripts to steal tokens or change settings. Slack issued an emergency fix, but enterprise customers demanded stronger security, diverting engineering resources for a week.**Atlassian Confluence (2021)**: A persistent XSS vulnerability in Confluence allowed users with certain permissions to insert malicious macros that hijacked sessions. Organizations reported unauthorized wiki edits, forcing Atlassian to release an urgent patch and enterprises to perform rushed updates.

## Explore other resources

## Frequently asked questions

### What are the three main types of cross-site scripting?


The three main types of XSS are persistent (stored), reflected, and DOM-based.

### What is the primary goal of cross-site scripting?


The primary goal of XSS is to execute malicious scripts in a victim's browser, often to steal data, hijack sessions, or manipulate website behavior.

### What is the difference between XSS and CSRF?


XSS exploits the user’s browser to execute scripts, while cross site request forgery (CSRF) tricks authenticated users into performing actions without their intent.

### How common are XSS attacks?


XSS attacks are among the most common web vulnerabilities, frequently appearing in the Open Web Application Security Project (OWASP) Top Ten Security Risks.

### What are the consequences of cross-site scripting?


Consequences of cross-site scripting include data theft, session hijacking, keylogging, phishing, and website defacement. For organizations, XSS can negatively impact customer trust and draw regulatory penalties.

### What is a good mitigation solution against XSS?


The most effective way to mitigate XSS attacks is to use a combination of input validation, output encoding, CSP, and secure coding practices.

### How do developers fix XSS vulnerabilities in code?


Code scanning tools like [GitHub Advanced Security](https://github.com/enterprise/advanced-security) help developers find and fix XSS vulnerabilities before they leak to production.

Cross-site scripting remains a significant threat to web security. By understanding its mechanics, types, and consequences, developers and organizations can adopt effective prevention and mitigation strategies. Proactive measures like input validation, output encoding, and client-side defenses help ensure robust protection against XSS vulnerabilities.