# openNLP

**Title:** Alternative GPT with Gemini API and Offline Capabilities

**Introduction:**

This project offers a cost-effective alternative to GPT by leveraging the Gemini API for online interactions and a locally trained model for offline scenarios. It aims to provide a robust chatbot with a 0% fail rate, ensuring continuous responses regardless of internet connectivity.

**Key Features:**

* **Cost-Effective Alternative:** Utilizes the free tier of the Gemini API for online interactions, reducing costs compared to traditional GPT solutions.
* **Dual Response Strategy:** Employs a combination of online and offline models to guarantee a response even without an internet connection.
* **Zero Fail Rate:** Ensures the chatbot can always respond to user queries, maintaining a seamless interaction experience.
* **Self-Learning (WIP):** This feature is under development and aims to enable the model to learn and improve through user interactions, similar to how we teach children.
* **Learning from Uploads (Work in Progress):** Future enhancements will allow the model to learn from uploaded datasets, expanding its knowledge base and improving its responses.

**Technical Overview:**

This section will be added once you provide more details about the implementation.  Here are some potential areas to cover:

* Programming language and libraries used
* Architecture of the online and offline models
* Details about the self-learning and upload learning functionalities (when implemented)

**Installation:**

(Provide instructions on how to install any required dependencies or packages)

**Usage:**

(Describe how to run the chatbot and interact with it, including any command-line arguments or configuration options)

**Current Limitations:**

* **Self-Learning and Upload Learning (WIP):** These features are currently under development and may have limited functionality.
* **Accuracy and Fluency:** As a young project, the model's responses may not always be perfectly accurate or fluent. We are actively working on improving its performance.

**Future Work:**

* **Refine Self-Learning:** Enhance the ability of the model to learn from user interactions.
* **Develop Upload Learning:** Implement functionality for the model to learn from uploaded data.
* **Improve Accuracy and Fluency:** Continuously improve the model's ability to generate reliable, informative, and engaging responses.
* **Expand Online Capabilities:** Explore advanced use cases with the Gemini API.

**Contributing:**

We welcome contributions from the community! If you're interested in helping, please feel free to open an issue or pull request.

**License:**

(Specify the license under which you distribute your code)

**Author:**

(Include your name or organization)

**Additional Notes:**

* Consider adding visuals (e.g., screenshots, diagrams) to enhance understanding.
* Use clear and concise language throughout the README.
* Maintain the README as the project evolves to keep users informed.

I hope this enhanced README.md file provides a comprehensive and informative overview of your project!

---

## Fix Errors (Solutions)

If You are getting error lie 
```sh
(aibot) myserver@myserver:~/Documents/openNLP$ python3 offlineNLP.py
Loading std-startup.xml...Traceback (most recent call last):
  File "/home/myserver/Documents/openNLP/offlineNLP.py", line 22, in <module>
    chatbot = Chatbot()
  File "/home/myserver/Documents/openNLP/offlineNLP.py", line 6, in __init__
    self.kernel.learn("std-startup.xml")
  File "/home/myserver/Documents/openNLP/aibot/lib/python3.10/site-packages/aiml/Kernel.py", line 335, in learn
    start = time.clock()
AttributeError: module 'time' has no attribute 'clock'
```

Solution: 

It appears that your code is using the `time.clock()` method, which was deprecated and eventually removed in Python 3.8. To address this, you can replace `time.clock()` with `time.process_time()`.

Here's the modified `Kernel.py` file:

```python
# File: aiml/Kernel.py

# Replace this line:
# start = time.clock()
# with:
start = time.process_time()
```

The `time.process_time()` method is used for measuring the CPU time, and it's the recommended replacement for the deprecated `time.clock()` method.

After making this change, you should be able to use your AIML code with Python 3.7 or later without encountering the `AttributeError` related to the `time.clock()` method.