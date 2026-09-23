# Hugging Face and VirusTotal collaborate to strengthen AI security

source: https://huggingface.co/blog/virustotal
published: Wed, 22 Oct 2025 00:00:00 GMT

Updated

# Hugging Face and VirusTotal collaborate to strengthen AI security

[Update on GitHub](https://github.com/huggingface/blog/blob/main/virustotal.md)

[VirusTotal](https://virustotal.com), the world’s leading threat-intelligence and malware analysis platform. This collaboration enhances the security of files shared across the Hugging Face Hub, helping protect the machine learning community from malicious or compromised assets.

TL;DR - Starting today, every one of the 2.2M+ public model and datasets repositories on the Hugging Face Hub is being continuously scanned with VirusTotal.

##
[
](https://huggingface.co#why-this-matters)
Why this matters

AI models are powerful but they’re also complex digital artifacts that can include large binary files, serialized data, and dependencies that sometimes carry hidden risks. As of today HF Hub hosts 2.2 Million Public model artifacts. As we continue to grow into the world’s largest open platform for Machine Learning models and datasets, ensuring that shared assets remain safe is essential.

Threats can take many forms:

- Malicious payloads disguised as model files or archives
- Files that have been compromised before upload
- Binary assets linked to known malware campaigns
- Dependencies or serialized objects that execute unsafe code when loaded

By collaborating with VirusTotal, we’re adding an extra layer of protection and visibility by enabling files shared through Hugging Face to be checked against one of the largest and most trusted malware intelligence databases in the world.

##
[
](https://huggingface.co#how-the-collaboration-works)
How the collaboration works

Whenever you visit a repository page or a file or directory page, the Hub will automatically retrieve VirusTotal information about the corresponding files. [Example](https://huggingface.co/Juronuim/xbraw2025/tree/main)

Here’s what happens:

- We compare the file hash against VirusTotal’s threat-intelligence database.
- If a file hash has been previously analyzed by VirusTotal, its status (clean or malicious) is retrieved.
- No raw file contents are shared with VirusTotal maintaining user privacy and compliance with Hugging Face’s data protection principles.
- Results include metadata such as detection counts, known-bad relationships, or associated threat-campaign intelligence where relevant.

This provides valuable context to users and organizations before they download or integrate files from the Hub.

##
[
](https://huggingface.co#benefits-for-the-community)
Benefits for the community

- Transparency: Users can see if files have been previously flagged or analyzed in VirusTotal’s ecosystem.
- Safety: Organizations can integrate VirusTotal checks into their CI/CD or deployment workflows to help prevent the spread of malicious assets.
- Efficiency: Leveraging existing VirusTotal intelligence reduces the need for repeated or redundant scanning.
- Trust: Together, we’re making the Hugging Face Hub a more secure, reliable place to collaborate on open-source AI.

##
[
](https://huggingface.co#join-us)
Join us

If you’d like to learn more about this integration or explore ways to contribute to a safer open-source AI ecosystem, reach out to [security@huggingface.co](mailto:security@huggingface.co).

Together, we can make AI collaboration not just open but secure by design.