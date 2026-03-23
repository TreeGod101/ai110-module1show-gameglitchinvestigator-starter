# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The things I found to be broken were the hints, game state, and attempts. For the hints they were opposite to what they should have been, for example if the secret was lower than my guess it would say go higher. For game state, after the first initial play it wouldn't let me play after pressing new game. Finally when you load up the app it uses one of your guesses already. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI tool I used for this project was Copilot. An AI suggestion I used was for the state session fix, I basically explained the problem (after having copilot explain the problem) and said what needed to be changed for it to be fixed. I verfied it would be correct by just directly testing the app manually to see if he new game state worked as I intended. For a bad suggestion it was telling me to initialize attempts to be 1. I felt as if this was wrong but I let it do it anyways to see how it would change anything. As I thought it made the amount of attempts you had -1 than the inteded amount so I switched it back to 0. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

The way I verified repairs and if bugs were fixed was by running it the same way I found the original bug. I manually went through the app and tried to break it or find the bug again and if I didn't see it happen, and it worked as how I logically though the process should work then I considered it fixed. AI helped me understand how the tests worked, I basically just asked it to explain to me how they worked and asked for it to run an "input" and walk me through it. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

In the original version of the app, the secret number reset because the actual initialized secret was never stored into each session, therefore refreshing it everytime you would give an input. From my understanding of Streamlit's reruns, its basically an app that rebuilds itself with every interaction, so like interacting witha  button or input. Session states are kind of like a checkpoint of all the important information that needs to be taken to the next state. So by using a session state you are basically retaining the information like a checkpoint and resetting to a new point. The change I made that gave a stable secret number was setting the if check to assign a random variable if the "secret" is not in st.session_state. This basically just made it so that it stayed in a single state and didnt change throughout every state change. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit or strategy I want to bring forward into future labs and projects is to logically break down the problems and issues, and not just blindly follow the AI. Something I would do differently is let ai write a lot of the code, I would at least read the documentation of what code it was writing next time. This project definitely showed me the instability of ai at times and also the amount of excessive inputs it gives. 
