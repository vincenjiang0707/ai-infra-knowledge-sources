source: https://github.com/resources/articles/what-are-ai-models

# What are AI models?

Learn how AI models work and how they can help your org.

## What is an AI model?

An AI model is a computer program that’s been trained to recognize data patterns, analyze data, and make predictions or decisions based on that data. AI models are built using algorithms and parameters that enable them to mimic human cognitive functions like reasoning, classification, and problem solving.

AI models continuously fine-tune their parameters based on the data they’re exposed to. This allows the models to improve their accuracy and performance over time and function well when faced with new, unseen data.

## How AI models work

AI models, which are sometimes called machine learning models or ML models, operate by numerically processing data, identifying patterns, and optimizing their predictions iteratively. Here's an overview:

**Numerical representation of data.**AI models require data to be numerically represented because they can’t process raw information. Text data is encoded using methods like word embeddings, which map words to vectors in a continuous space, and tokenization, which breaks text into smaller units, or tokens. Likewise, images get converted into pixel arrays. These representations capture the underlying features of the data that an AI model analyzes.**Pattern identification during training.**During training, an AI model learns data patterns and relationships by adjusting its internal parameters. This process can involve feeding labeled examples to the model, known as supervised learning. Or it can involve allowing the model to infer structure, known as unsupervised learning. Models such as neural networks use multiple layers to extract increasingly abstract features. For example, in customer service chatbots, AI models learn how to effectively understand and respond to customer queries.**Mathematical foundations of learning.**An AI model’s learning process is grounded in optimization techniques like gradient descent, which involves calculating the error, or loss, between the model's predictions and the actual values, then updating the model's parameters to minimize this error. In addition, backpropagation, a key algorithm in neural networks, efficiently computes gradients for parameter updates across neural network layers.**Generalization of new data.**Once trained, an AI model applies its learned knowledge to make predictions or decisions on new inputs. The ability to generalize or accurately interpret data it hasn’t seen before is critical to an AI model's usefulness in real-world applications. For instance, predictive maintenance in manufacturing uses AI models to foresee equipment failures and schedule timely repairs.**Iterative optimization and error minimization.**Training is an iterative process with AI models continuously adjusting their parameters to reduce errors. Techniques like learning rate scheduling, regularization, and validation help the model fit the training data and perform well on unseen data.

## What AI models can do

AI models help organizations across industries improve efficiency, reduce operating costs, and identify new opportunities by addressing complex problems and adapting to evolving demands.

Here are some key capabilities of AI models and their real-world applications:

**Data analysis and prediction.**AI models excel at analyzing vast amounts of data to forecast outcomes. For example, in finance, predictive models assess market trends by analyzing past and present data, evaluating market events, and incorporating economic indicators. They also detect fraudulent transactions by identifying unusual banking, spending, and investment patterns. And in healthcare, AI models help predict patient diagnoses and treatment responses.**Natural language understanding and generation.**Models like transformers power[AI agents](https://github.com/resources/articles/what-are-ai-agents)such as chatbots and virtual assistants. Businesses use these to answer customer questions and resolve customer complaints more efficiently. These models can also be used to analyze customer sentiment in reviews, surveys, and social media. They also can instantly translate text from one language to another.**Computer vision.**AI enables machines to “see” and interpret images and videos. In manufacturing, this helps improve quality control by quickly detecting product defects. In agriculture, drones equipped with AI-powered vision systems can monitor crop health and detect pest infestations. And in security, facial recognition helps enhance identity verification systems.**Automation and optimization.**AI optimizes processes by automating repetitive tasks. For example, in logistics, AI models can help optimize transportation routes in real-time as weather and other travel conditions change. And the retail and entertainment sectors use AI models for personalized recommendations of products and streaming content.**Creative problem solving.**[Generative AI models](https://github.com/resources/articles/what-are-generative-ai-models)can create realistic content, including written text, images, videos, logos, music, sound effects, programming code, and product prototypes. The entertainment and marketing sectors have already found numerous applications for generative AI. The gaming industry is using AI to develop realistic virtual environments and character behaviors to enhance player experiences.

## Types of AI models and examples

There are several different types of AI models. Each offers unique capabilities and performs specific tasks based on how they learn and process data. Here's an overview of the different types of AI models and what each can do:

**Supervised learning models.**These models learn from labeled datasets, where the input and output parameters are both provided. They excel at tasks like classification and regression and are useful for predicting customer churn, detecting fraudulent transactions, and recognizing images. Decision trees, support vector machines, and neural networks are types of supervised learning models.**Unsupervised learning models.**These models identify patterns and structures in unlabeled data without predefined outcomes. They are ideal for tasks like clustering, detecting anomalies, and reducing the number of features in a dataset. Business applications include customer segmentation, credit card fraud detection, and recommendation systems.**Deep learning models.**A subset of machine learning, these models use neural networks with multiple layers to manage complex tasks that require high-level abstraction. Examples of deep learning models include[natural language processing](https://github.com/resources/articles/natural-language-processing)(NLP) models like ChatGPT and Claude Sonnet. Real-world applications for NLP models include self-driving cars and computer vision capabilities like image and facial recognition.**Generative models.**These models create new content like text, images, music, and videos based on learned data patterns. Generative adversarial networks and transformers are some of the techniques used in generative models. Business applications of these models include summarizing text, generating synthetic data that looks like real data, and assisting product design and software development.**Reinforcement learning models.**These models learn by interacting with an environment and receiving feedback in the form of rewards or penalties. They are commonly used for decision making and sequential tasks. Robotics, game development, and real-time bidding in online advertising are some real-world applications for reinforcement learning models.**Hybrid models.**These models address complex problems by combining multiple AI approaches, drawing on the strengths of each. For example, self-driving cars use supervised learning for object detection, unsupervised learning for mapping, and reinforcement learning for navigation.

## How AI models are trained

Training AI models is a structured process that transforms raw data into systems that can generate predictions or insights. AI model training consists of multiple stages, each of them critical to creating robust and effective solutions:

**Prepare the data.**AI models rely on large, high-quality datasets to learn effectively. Data must be cleaned and prepared to help ensure consistency, remove noise, and address missing or incorrect values. For instance, source code for software may require quality and security verifications. Without clean data, models are more likely to produce inaccurate or biased results.**Choose a model type.**Select which AI model type to use based on the nature of the data, complexity of the task, and desired outcome. For example, you might want to train models on high-quality code in languages that your development teams use.**Teach the model.**During training, the model uses algorithms to learn patterns in the data. For example, neural networks adjust weights across layers to identify complex relationships, while decision trees split data into branches for easier classification. The model iteratively refines its parameters to minimize error and improve accuracy.**Evaluate performance.**Once trained, model performance is evaluated using metrics like accuracy, precision, recall, and F1 score, depending on the problem type. The model is also tested on unseen validation data to measure its ability to generalize beyond the training dataset. This helps ensure that it is not overfitted to specific examples.**Deploy in real-world systems.**Trained models are deployed into production environments where they interact with real-world data. For example, a customer service chatbot can process live queries, or a recommendation engine can generate product suggestions that are personalized for each user. Deployment involves integrating the model into workflows and ensuring it runs efficiently at scale.**Continuously monitor and retrain.**AI models require ongoing monitoring to maintain accuracy as data patterns evolve. Over time, a model's predictions may degrade due to changes in user behavior, market trends, or other factors. Retraining the model on updated datasets helps it remain relevant and reliable.

## The impact of AI models on software development and security

AI models are revolutionizing the development world by automating routine and complex tasks, increasing efficiency, fostering creativity and innovation, and allowing development teams to focus on higher-value projects.

Let’s look at some of the biggest impacts that AI models are having on technology professionals and teams:

**Transforming software development.**AI-powered tools like GitHub Copilot assist developers by generating code snippets, suggesting new edits in response to code changes, and even creating development plans to define new features and applications. This helps reduce the time spent on repetitive and administrative tasks, accelerate development cycles, and allow teams to spend more time building creative, innovative solutions. For example, developers can use[AI code generation](https://github.com/resources/articles/what-is-ai-code-generation)to explore alternative coding approaches, build prototypes faster, and expedite time to market.**Enhancing security during development.**AI models help strengthen security by identifying potential data vulnerabilities, anomalies, and irregularities during coding. Tools like GitHub Copilot can suggest secure coding practices like validating user inputs to prevent injection attacks. They also can detect hardcoded secrets, prompting developers to use environment variables instead. By identifying bugs and security flaws early in the development process, AI models help reduce the likelihood of security vulnerabilities during production.**Freeing developers to do what they do best.**By automating repetitive and time-consuming tasks, AI tools allow developers to concentrate on problem solving, strategic decision making, and the creative aspects of software design. Teams can allocate more energy to building robust, scalable, and innovative systems, while AI manages the groundwork.

As AI evolves, it’s likely to play a larger role in software development Adding AI-powered tools to your organization’s development process enables your teams to work more efficiently, improve code quality, and strengthen security throughout the software development life cycle.

## Explore other resources

## Frequently asked questions

### What are types of AI models?


There are various types of AI models, including:

Supervised learning models that are trained on labeled data for tasks like classification and regression.

Unsupervised learning models that find patterns in unlabeled data.

Deep learning models or neural networks for tasks like image recognition and natural language processing.

Generative models like generative adversarial networks for creating new data.

Reinforcement learning models that learn by optimizing actions based on feedback.


### What are AI models used for?


AI models are used to perform a broad range of functions across industries. They power real-world applications like predictive analytics, fraud detection, recommendation systems, image and speech recognition, natural language processing, and automation. For example, AI models enable self-driving cars to navigate roads, virtual assistants to process queries, and healthcare systems to identify disease patterns in medical data.

### What are some examples of AI models?


Examples of AI models include generative AI tools like ChatGPT and Claude Sonnet. Different types of AI models can generate text, classify images, generate time-series data like stock prices and website traffic, and interpret and forecast data. AI models are used in tools like GitHub Copilot for code suggestions, fraud detection systems in the banking industry, and autonomous vehicle technology.

### How do AI models get trained?


AI models are trained using large datasets that represent the task at hand. The data is cleaned and preprocessed, then fed into the model during training. Algorithms such as gradient descent adjust the model’s parameters iteratively to minimize errors. After training, models are typically tested on unseen data to evaluate their performance and ability to generalize before deployment.

### How are AI algorithms trained?


AI algorithms are trained by exposing them to data and iteratively refining their parameters based on feedback from a loss function. Techniques like backpropagation calculate how much each parameter needs to be adjusted by computing gradients, which show the direction and size of the changes. This process is repeated across multiple training epochs, or passes through the training dataset, to improve accuracy. Training may involve supervised learning with labeled data, unsupervised learning with unlabeled data, or reinforcement learning through reward-based feedback.

### How are AI language models trained?


AI language models are trained on vast bodies of text data using neural networks like transformers. These models learn to predict the next word in a sequence by analyzing patterns in grammar, syntax, and meaning. Pretraining involves general language understanding, while fine-tuning tailors the model for specific tasks, such as providing summaries or answering questions. Training requires significant computational resources and is optimized using methods like gradient descent and large-scale parallel processing.