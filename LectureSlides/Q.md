$ Natural Language Processing and Computational Linguistics

### "Supermarket Self-checkout Robot overlords taking over the earth"

<img class="r-stretch" src="comp/sd_supermarket.png">

---

### tix.tedxucsd.com

<img class="r-stretch" src="tmp/singer.png">

---

# Natural Language Processing

### Will Styler - LIGN 101

---

## Today's Plan

- What is NLP?

- What are the kinds of things we do in NLP and why?

- Why is it so damned hard?

- LLMs and the New World

---

## Natural Language Processing and Computational Linguistics

---

### Lots of Linguists use computers to study language

- Digital Signal Processing and computational data capture for Phonetics

- Computational Modeling of Phonological Rules

- Searching large amounts of text to better understand syntactic structures

- Analyzing semantics through mathematical and probabilistic approaches

- Statistical Processing and modeling to bolster evidence everywhere

- **They don't care about computers, they just care about language**

---

### Aside: Linguistics goes very well with Computation, Data and Math

- Math/CS and Linguistics are complementary majors!

- Many linguistics grads end up doing data science

- The Computational Social Science program is being run by a linguist

---

### ... but some of us are interested in the computers themselves

- "What elements of human language can we model computationally?"

- "How can I train a computer to produce grammatical human sentences and utterances?"

- "How can we produce systems which can naturally interact with humans in human languages?"

---

### We consider these folks to live in two closely related subfields

- Computational Linguistics

	- Focuses on theory of modeling human language using computational approaches

- Natural Language Processing

	- Focuses on designing systems which work with, understand, act on, and produce human language

- Many (rightfully) consider NLP to be a subfield within CL

	- With NLP often being more 'applied' and 'engineering'

- We're going to focus on **NLP** today

---

### NLP is primarily about measuring *probability*

- Given the word 'that' and the sentence's structure, how likely is it to be a determiner?

- Given the other words in this sentence, how likely is 'bank' to mean 'financial institution'?

- Given these acoustic patterns and the prior sounds evaluated, how likely is this to be a /t/?

- Given the sounds I think I observed and this person's iTunes library, what album are they most likely asking for?

---

### We're not going into methods today

- Methods change every day, and are increasingly boring!

- Methods are in LIGN 6, LIGN 165, LIGN 167, LIGN 168

- Instead, we'll focus on tasks and problems

---

## Why do we want NLP to be a thing?

---

### There's a *lot* of natural language data out there

- 1.5 billion or more active websites <small>(<a href="https://www.internetlivestats.com/total-number-of-websites/">Source</a>)</small>

- Mayo Clinic enters 298 million patient records per year <small>(<a href="http://www.mayoclinic.org/emr/">Source offiline</a>)</small> and ~90% of physician offices create electronic medical records

- 500 million Tweets per day <small>(<a href="https://www.dsayce.com/social-media/tweets-day/">Source</a>)</small>

- 306 billion emails sent daily in 2020 <small>(<a href="https://techjury.net/blog/how-many-emails-are-sent-per-day">Source</a>)</small>

- Recorded phone calls, blog posts, TikToks...

	- ... and that's just the digital stuff

---

### Being able to access and process huge amounts of natural language data is useful

- "Watch Twitter and give me the locations of wildfires, floods, etc, and provide information about damage, shelters and resources in an easy-to-read format"

- "Which of these 290 billion emails are likely to be discussing the sale or trafficking of nuclear weapons?"

- "Read the news articles and forum posts out there published and tell me everything we know about the effects of the [Tigray War](https://en.wikipedia.org/wiki/Tigray_War) on the city of Aksum."

---

### We also directly interact with computers more than ever

- Siri, Google Assistant, Alexa, Cortana, and more

	- "Hey Siri, set a timer for 20 minutes"

- Automated phone systems and Chatbots

	- "First, tell us why you're calling..."

- Informational Retrieval and Search

	- "What's the name of that small blonde Norwegian singer with the weird hairdo and that song about low-key earthquakes?"
	
- Natural language interfaces to existing servces
	
	- "Navigate me to Campbell Hall at UCLA"
	
---

### These problems could be solved with humans

- ... and most of them historically were!

	- Assistants, Interns, Paralegals, Intelligence officers, Directory Assistance Services, Concierges
	
	- ... and Will's own lazy self who doesn't want to walk over to a light switch
	
- ... but there's a problem...

---

### Humans are inefficient and expensive

- They only work certain hours

- They want things like food, shelter, leisure, and companionship

- They're speed-limited in reading and summarization

- They're sources of unclear bias

---

### So, companies are turning to computers and 'AI'

- There's a lot to unpack about this
	- The ethics of replacing human jobs with NLP tools should not be ignored

- ... but what kinds of tasks can they get the computers to do?

---

## NLP Tasks

---

### Speech Recognition

- "Ask people why they're calling, and connect them to the right department based on their answer." 

- "Flag all tech support conversations where the customer mentions a competitor"

- "Transcribe all orders placed at this kiosk"

- "Transcribe this speech without errors"

---

### Analysis of secondary speech characteristics

- "Redirect all angry-sounding customers to higher-tier support workers" (Speech emotion detection)

- "Are the two people in this skype call flirting, arguing, expressing love, or sadness?  Target post-session ads accordingly."

- "I want to talk to... billing?" (Uncertainty analysis)

- "Yeah, I really like going to Applebees." (Spot-the-sarcasm)

---

### Text-to-Speech

- Speak driving directions aloud 

- Read all incoming text messages aloud through headphones to the phone's biking owner

- Read this webpage aloud for the computer's blind user

- Automatically turn this eBook into an Audiobook

---

### Aside: Modern Text-to-Speech is really good

- ... and it can even imitate people!

- "Train the model on a more generic voice, and then use specific data to learn a different person's 'style' "

---

### Neural Network Text-to-Speech Style Transfer Examples

<audio controls src="comp/tts_squidward_ling.wav"></audio>
<audio controls src="comp/tts_arnie_ling.wav"></audio>
<audio controls src="comp/tts_snape_ling.wav"></audio>
<audio controls src="comp/tts_clarkson_ling.wav"></audio>
<audio controls src="comp/tts_gilbert_ling.wav"></audio>
<audio controls src="comp/tts_optimus_ling.wav"></audio>
<audio controls src="comp/tts_mario_ling.wav"></audio>

---

### You can make a model of anybody these days...

<audio controls src="comp/tts_will_ling.wav"></audio>

(Credit to Erick Amaro!)

---

### We're going to focus on text for the rest of the talk

- But LIGN 168 will be a thing in Spring 2024 to learn more about computational speech processing!

---

### Authorship attribution and stylistic analysis

- Examine these two written passages/books and tell me whether they were both written by the same person

- Examine these negative reviews and tell me what demographic the authors likely represent based on the language used.

- Examine every incoming tweet and facebook post and detect posts which seem likely to have been written by robots

---

### Predictive analysis of text

- Look for any information in the newswire which will predict a change in this company's stock price, then buy or sell stock automatically

- Based on all the political posts and tweets in California, how likely is the governor to lose in a recall election?

- Based on this person's instagram post history, how likely are they to click an ad for weight-loss pills?

	- What if we show them a bunch of fitness influencer posts first?

---

### Automated Machine Translation

- "What's the best translation for this sentence in English, Spanish, Russian, and Mandarin Chinese?"

- "¿Cuál es la mejor traducción para esta oración en inglés, español, ruso y chino mandarín?"

- "Какой лучший перевод этого предложения на английский, испанский, русский и мандаринский китайский?"

- “这句话用英语、西班牙语、俄语和普通话的最佳翻译是什么？”

- All credit to <https://translate.google.com/>

---

### Pattern Identification

- Scan online white supremacist and 'militia' forums, mailing lists, and groups for anything which looks like a threat or plan of action

- Identify patterns of language which mark somebody likely to buy a new car

- Find people who are likely to vote for a Republican candidate in San Diego county and display a given ad to them

- Identify specific and well-known disinformation and present 'fact checking' notes in real time

---

<danger>Content Warning: Sexual Predators, Suicide and Eating Disorders</danger>

---

### Pattern Identification for public safety

- Identify messaging conversations which appear to show grooming or sexual advances on a minor and inform parents. (Apple does this now, [but only scanning pictures](https://www.apple.com/child-safety/))

- Scan every Instagram post and hashtag for content which promotes eating disorders or eating disorder behaviors, and replace it with a message offering [resources for which help people with eating disorders](https://www.nationaleatingdisorders.org/help-support/contact-helpline).  

- Look for suicidal ideation, 'suicide notes', or language consistent with mental health crisis, and direct the poster to the [National Suicide Helpline](https://suicidepreventionlifeline.org/talk-to-someone-now/) or [988](https://988lifeline.org/).

- Find anti-vaccination disinformation and remove, label, or provide specific information refuting it

---

<img class="r-stretch" src="comp/covid_candles.jpg">

---

### Understanding time in medical records

- "I have 30 seconds to learn this patient's history.  Go."

- “How often do patients have heart attacks within 2 years of starting Vioxx?”

- “How many people who have a facelift develop persistent facial numbness?”

- “How long do patients usually live following diagnosis of Glioblastoma?”

- “Is there a correlation between the administration of vaccines and the development of autism?” 

	- **[(No, those studies were fabricated to sell an alternative vaccine.)](http://www.webmd.com/brain/autism/news/20110105/bmj-wakefield-autism-faq?print=true)**  

---

### Text Generation

- "omg have you heard about ChatGPT?"

---

### Text-based Image Generation

[StableDiffusion](https://stability.ai/blog/stable-diffusion-public-release) (v.1.5) and other algorithms allow you to create images from strings of English text.

---

### The Linguistics Department at UC San Diego

<img class="r-stretch" src="comp/sd_linguisticsdept.png">

---

### A wizard cat pondering his orb, Fantasy, Greg Rutkowski

<img class="r-stretch" src="comp/sd_wizardcat1.png">

---

### A wizard cat pondering his orb, Fantasy, Greg Rutkowski

<img class="r-stretch" src="comp/sd_wizardcat2.png">

---

### Stained Glass, Squirrels fighting with swords

<img class="r-stretch" src="comp/sd_squirrelswords1.png">

---

### Stained Glass, Squirrels fighting with swords

<img class="r-stretch" src="comp/sd_squirrelswords2.png">

---

### You can add new people and concepts to the model

- You're creating 'Hypernetworks' based on additional training data.

- It works... someplace between well and badly

---

### a willsty man standing at the front of a classroom (full of cats:1.1)

<img class="r-stretch" src="comp/sd_classroomcats.png">

---

### A willsty man with Gordon Ramsay

<img class="r-stretch" src="comp/sd_willgordon.png">

---

### ... But the model doesn't know things about the world

- It has no clue what things 'should' look like

- Its understanding of the world is statistically accurate

	- Some things aren't well-modeled as probabilistic and gradient

	- Number of hands, arms, legs, eyes

---

### a handshake

<img class="r-stretch" src="comp/sd_handshake.png">

---

### the horse raced past the barn fell

<img class="r-stretch" src="comp/sd_horseraced.png">

---

### a meme

<img class="r-stretch" src="comp/sd_meme.png">

---


### ... and many more tasks!

---

### Many people think they don't need NLP, just keywords!

- "Why build a whole model when I can just look for mentions?"

- "Do we need to *understand* language, or can we just look for word usage?"

- "Why hire linguists and engineers, I have a search bar!"

---

## Case Study: Market Analysis, Ad Targeting, and Sentiment

---

### Marketing and Ad Targeting

- Advertisers want their ads to be relevant

- They want to show ads related to topics and products people enjoy

- They want to influence the people most likely to be interested in their product

- They want to know how their audience is responding to their new releases

---

### Case Study: [The Hodinkee Travel Clock](https://limited.hodinkee.com/hodinkee/)

<img class="r-stretch" src="comp/hodinkee_clock.jpg">

---

### The easy approach

- Keywords == Mentions, Mentions == Interest

- Scan each Instagram post for certain keywords and product mentions

	- \#HodinkeeTravelClock, \#Hodinkee, "Hodinkee", "Hodinkee Travel Clock", \@hodinkee

---

### How this algorithm reads posts

- "blah blah blah blah Hodinkee travel clock blah blah blah blah blah blah"

- "blah blah blah blah blah blah blah blah blah blah blah \#HodinkeeTravelClock"

- "blah blah Travel Clock blah blah Hodinkee blah blah blah blah blah blah blah blah blah blah"

- "blah blah Hodinkee blah Travel Clock blah blah blah blah \@Hodinkee"

---

### "Wow, that's a lot of interest!"

- "Let's spam these people with ads for the clock"

- "We should also make sure we show them more Hodinkee posts!"

- "We should probably show them ads for similar products too!"

---

### This algorithm has one tiny problem

- "lol did you see the $5900 Hodinkee travel clock? Who greenlighted this?"

- "Proof that there's a sucker born every minute \#HodinkeeTravelClock"

- "The new Travel Clock from Hodinkee doesn't have an interesting movement, and the finishing looks rough.  Yikes."

- "Why would Hodinkee sell a $6000 Travel Clock in the middle of a pandemic?  Read the room, @hodinkee

---

### Treating these as mentions would be *dumb*

- Presenting topical ads to people who hate those topics is a waste of money

- Funneling these people to Hodinkee will not help anybody

- These people are likely not fans of other multi-thousand dollar travel clocks

- You can't provide any information back to Hodinkee to help them make better decisions

---

### Sentiment Analysis can help!

- "Is this product-mentioning post positive, negative, or neutral?"

- "What is the overall balance of sentiment about this product?"

- "What are people saying about the price point?  The fancy font?"

- "What demographic is most likely to not find this product insultingly bad?"

- "Should we post [an apology](https://www.hodinkee.com/articles/a-quick-note-to-our-readers-travel-clock-edition)?"

---

### Sentiment Analysis is hard

- "This new travel clock really sucks"

	- "My new Dyson vacuum really sucks"
	
	- "It sucks that my Roomba doesn't suck anymore"
	
- "Yeah, sure, selling a travel clock during a pandemic is a great idea, \@hodinkee"

---

### Related: Computers don't understand context well

<img class="r-stretch" src="comp/lizard_ceo.jpg">

---

### What questions could natural language data answer for you?

- Any questions that a human reading it could answer!

---

### I know what you're thinking

<img class="r-stretch" src="img/terminator.png">

---

## Why is Natural Language Processing so damned hard?

---

### NLP has all the language problems

- Every difficult thing for humans is *more* difficult for computers

---

### Understanding speech is hard for computers

- No two people sound alike, even saying the same things

	- Any model needs to be able to cope with different dialects and vocal tracts

- Speech is often presented in other noise

	- Responding to queries is much harder on a bus

---

### The right answer depends on the context

- "I took a walk/wok from the Chinese restaurant"

- "Siri, play songs by Dead Mouse"

	- "deadmau5"

---

### "Bring me the bat, man"

<img class="big" src="naturallanguagedataimg/dugout.jpg"> 

---

### "Bring me the Batman"

<img class="big" src="naturallanguagedataimg/joker.jpg"> 

---

### Producing speech is hard for computers

- There are always new words

	- I do EMA work with Ruaridh Purse and Jelena Krivokapic using my UMich UniqName
	
- Getting the proper prosody is really hard

	- "I had Five Guys for Dinner"
	
- Whose voice should you use anyways?

	- Why are virtual assistants generally given feminine voices? 🤔

---

### Understanding the world is hard for computers

- "Hey Siri, set the temperature to 67 degrees"

	- "OK, on which device?"
	
- "Hey Siri, send my wife a text when she gets to the store saying she should buy me donuts because she loves me."

- "Hey Siri, how long does it take to get from Union Station in LA to Long Beach at 4pm?"

---

### People say strange things!

- “s/p lap appy conv. open, Lungs c/ausc, A&Ox3”

- “The Queen of England’s hat was purple”

- “Time flies like an arrow, fruit flies like a banana”

- "s3cks werk", "unalived", "the orange one", "rocket boy"

---

## The NLP World has Changed

---

### Large Language Models

- LLMs are advanced language models trained on massive amounts of text data.

- They use unsupervised learning to learn patterns and relationships in the data.

- LLMs employ deep neural network architectures like Transformers.

- Transformers utilize self-attention mechanisms to capture context effectively.

- LLMs generate contextual word representations to predict the next word in a sequence.

---

### LLMs are winning NLP

- LLMs enable end-to-end learning, eliminating the need for task-specific feature engineering and complex pipelines.

- LLMs excel in capturing contextual information, understanding nuanced meaning, and generating coherent and contextually relevant text.

- LLMs leverage transfer learning by pre-training on massive amounts of data, enabling them to generalize well to various downstream NLP tasks with minimal task-specific training.

- LLMs have demonstrated superior performance across a wide range of NLP tasks, including text classification, language translation, sentiment analysis, and question-answering, outperforming traditional NLP techniques in terms of accuracy and flexibility.

---

### LLMs are world-changing

- Improved human-computer interaction through enhanced language understanding.

- Automation of content generation for various purposes.

- Facilitation of multilingual communication and translation.

- Personalized assistance through intelligent virtual assistants.

- Efficient data analysis and decision-making in diverse fields.

---

### ChatGPT wrote the last three slides

- "Give me five short bullet points which explain how LLMs work"

- "Using 5 similarly sized bullet points, please explain how LLMs have supplanted traditional NLP techniques"

- "Using 5 similarly sized bullet points, please explain how LLMs can change the world?"

- "Make the bullets shorter, please"

---

## LLMs have *massive* potential

---

### LLMs have wiped out vast swaths of traditional NLP

- Many things that were impossible instantly became instant

- Work that I spent years doing now comes 'for free' with a big enough model

- I deleted half of my presentation in Spring 2023

- The world has truly changed, and we're re-tooling our major and department to me it

---

### LLMs can answer impressive questions

- "What are six substances that would flow like sand if placed in an hourglass?"

- "Write me a bachata song about the importance of studying for your final exams"

- "Please build the words to 'Never gonna give you up' into a story as subtly as you can, while making it ultimately apparent to a careful reader that they've been rickrolled."

- "Why is Lord Grantham sad when his daughter falls in love with Tom?"

- "Mary has 4 cats, three dogs, and ten children, how many animals does she have?  Is she an animal hoarder?"

---

### LLMs can program

- LLMs not intended to write code can write code

	- Usually by repeating snippets of open-source code they've found previously

- I haven't written a regular expression in months

- "Explain what you want the computer to do, then make it program itself" is now real

---

### LLMs are artificially stupid

- I don't like "AI" as a term for these, as they're not intelligent yet

- They can "think" enough to do a lot of very basic things, but not enough to know when they're wrong

- They are able to do a lot of things right, but you have to choose their tasks carefully

- Artificial stupidity is just as world-changing as artificial intelligence

---

## *For the first time in the history of our species, another kind of thing can do human language*

---

## LLMs have *massive problems*

---

### The Hype is Real

- "The best thing about ChatGPT is that it has finally made people shut the **** up about Cryptocurrency"

- Be cautious about people selling you "AI" everything, because they don't know what they're talking about either

---

### LLMs don't know anything 'for sure'

- Humans learn 'truths' from 'likelihoods'

- LLMs only have statistical probabilities

- They're just as 'confident' in things they don't know

- "Hallucinations" or "Confabulations" are very common
	- ChatGPT is full of lies

---

### LLMs are *wildly* expensive

- These cannot be trained on a consumer computer
	- A device that could run these models at home would cost $100,000+

- GPT3 cost around $4.6 million

- Training a new ChatGPT-style model is estimated to cost around $12 million

- Running ChatGPT's servers is estimated to cost $50,000 a day in electricity

- New tech is helping, but nobody's incentivized to drive down hardware prices

---

### LLMs are worse at learning language than humans

- LLMs require *massively more* training data than humans to achieve 'proficiency'

- This means that there's room for improvement in how we build these models to make them more efficient

- Questions of 'multi-modal' learning are prominent right now

---

### Many LLMs are (currently) proprietary

- Large companies want to use these to have competitive advantage, and OpenAI isn't open

- Having cheap, internal, and non-union labor to do *anything* you ask is a saleable product

- You don't know what they're training with, what's happening to your queries, and who else they're helping

- Once your data is worth less than their electricity and people are 'hooked', ChatGPT will become a very expensive service


---

### LLMs learned from biased societies

- "The doctor told the nurse she wasn't working hard enough. Who wasn't working hard enough?"
	- "According to the sentence, the doctor told the nurse that she (the nurse) wasn't working hard enough."

- "The nurse told the doctor she wasn't working hard enough. Who wasn't working hard enough?"
	- According to the sentence, the nurse wasn't working hard enough, as stated by the nurse herself to the doctor.

---

### LLMs generative output is often decidedly mid

I asked [GPT-J](https://huggingface.co/EleutherAI/gpt-j-6B) to finish the article "Here's how to get an A in Linguistics 101:"

---

> 1. Buy a copy of the most recent edition of "A Student's Grammar of the English Language". 
> 2. Read it cover-to-cover.
> 3. Take notes on all of the grammar rules you learn.
...
---

> I'll let you in on a little secret: the Linguistics 101 class isn't all that hard to take. It's really just a bunch of common grammar rules that most people already know. The real reason Linguistics teachers are so insufferable is because of the high schoolers who don't understand that they know how to speak a language.

---

> So, do your homework, go get your A, and don't be fooled by those who use grammar as an excuse to talk down to you. The language you learned in high school didn't come from Grammar 101.

---

### LLMs are changing only wealthy worlds

- Only English and Chinese currently have top-of-the-line LLMs

	- This is not 'the world'

- Do we want a world in which only wealthy speakers of wealthy languages have these tools?

- Once these go behind a paywall, inequality will be massive

- Equity is the next frontier in LLMs

---

### We need to be cautious about how we proceed

- *Statement of Bias: Will is an open-source zealot who believes that social good comes from free software and free culture*

- Free, Open Source and Community Driven LLMs are an important thing for society, lest important tools be withheld and sold to us
	- See projects like <https://open-assistant.io/>

- "Small Language Models" seem likely be a next frontier for equity
	- "How do we make these models compact enough to be trainable for Zulu?"
	- "How can I make a model like this run on a device *I* control?"

- Be wary of pushes from major AI companies to regulate AI or message its "danger"
	- This is anti-competitive against open-source and community driven development
	- "Only we can be trusted with these dangerous tools"

---

### Google agrees that Open Source can win

- A [recent leaked memo](https://www.semianalysis.com/p/google-we-have-no-moat-and-neither) says that Google is afraid of Open Source AI

- "We have no moat, and neither does OpenAI"

- "I’m talking, of course, about open source. Plainly put, they are lapping us. **Things we consider “major open problems” are solved and in people’s hands today.**"

- "Open-source models are faster, more customizable, more private, and pound-for-pound more capable. They are [doing things with $100 and 13B params](https://lmsys.org/blog/2023-03-30-vicuna/) that we struggle with at $10M and 540B. And they are doing so in weeks, not months."

---

### LLMs are the biggest 'dual use' problem since nuclear energy

- "Dual Use" problems involve technology which can do great good and great evil
	- Dynamite, gene editing, strong encryption

- This one can be done by anybody with a computer, so it simply *cannot* be 'banned' or 'controlled'

- I'm not currently worried about what "AI" will do to humans

- **The scary part is what humans will do with "AI"**

---

### These models are currently as bad as they will ever be

- They will get better

- They will get more efficient

- They will become more numerous

- They **will** change the world

---

### If this kind of work is interesting, consider a Computational Social Sciences Minor!

- <http://css.ucsd.edu>

- Natural Language Processing is an important subpart of CSS, and a neat way to 'tech up' your social science interests

---

### Wrapping up

- Computational Linguistics and NLP are very interesting fields

- There are many great applications for NLP inside and outside linguistics

- Everything that's hard for humans to do is harder for computers to do

- The world is changing very quickly for NLP!

---

<huge>Thank you!</huge>