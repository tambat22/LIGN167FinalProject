$ Natural Language Processing and Computational Linguistics

### Supermarket Self-checkout Robot overlords taking over the earth

<img class="r-stretch" src="comp/sd_supermarket.png">

---

# Natural Language Processing

### Will Styler - LIGN 101

---

## Today's Plan

- What is NLP?

- What are the kinds of things we do in NLP and why?

- Two case studies

- Why is it so damned hard?

---

# Natural Language Processing and Computational Linguistics

---

### Lots of Linguists love computing

- Digital Signal Processing and computational data capture for Phonetics

- Computational Modeling of Phonological Rules

- Searching large amounts of text to better understand syntactic structures

- Analyzing semantics through mathematical and probabilistic approaches

- Statistical Processing and modeling to bolster evidence everywhere

- **This is why Math/CS/Data Science and Linguistics are complementary majors!**

---

### Here, computers are a means to an end

- "I'm going to use computers to better analyze human language so I can better understand humans"

- "I don't care what the computers do, I'm just better at doing my work this way"

- **Most linguists are using computers as tools to understand language**

---

### ... but some of us are interested in the computers themselves

- "What elements of human language can we model computationally?"

- "Can we teach computers to understand and produce human speech?"

- "How can I train a computer to 'understand' a sentence?"

- "How can I train a computer to produce grammatical human sentences and utterances?"

- "How can we produce systems which can naturally interact with humans in human languages?"

---

### We consider these folks to live in two closely related subfields

- Computational Linguistics

- Natural Language Processing

---

## Computational Linguistics ('CL')

The study of the theory and practice of modeling human language and grammar using computational methods, approaches, and tools

- "What elements of human grammar can be modeled using computational approaches and how?"

- CL is often a *theoretical* discipline

---

## Natural Language Processing ('NLP')

The study of the use of computational methods to analyze, understand, act on, and produce human language

- "How can we design systems which allow computers to analyze language and interact with humans using human language?"

	- The last bit is what distinguishes it from Human-Computer Interaction study ('HCI'), which has a broader focus.

- NLP has theory, but it is often more of a *practical* and *engineering* discipline

---

### CL and NLP folks coexist happily

- The problems are very similar, but with different goals

- Many (rightfully) consider NLP to be a subfield within CL

- We're going to focus on **NLP** today, but that's because it's a passion for Will!

---

### NLP is primarily about measuring *probability*

- Given the word 'that' and the sentence's structure, how likely is it to be a determiner?

- Given the other words in this sentence, how likely is 'bank' to mean 'financial institution'?

- Given these acoustic patterns and the prior sounds evaluated, how likely is this to be a /t/?

- Given the sounds I think I observed and this person's iTunes library, what album are they most likely asking for?

---

### We're not going into methods today

- Instead, we'll focus on tasks and problems

- Methods are in LIGN 6, LIGN 165, LIGN 167

	- Potentially also Computational Speech Processing
	
- ... but first, why do NLP?
	
---

## Why do you want NLP to be a thing?

---

### There's a *lot* of natural language data out there

- 1.5 billion or more active websites <small>(<a href="https://www.internetlivestats.com/total-number-of-websites/">Source</a>)</small>

- Mayo Clinic enters 298 million patient records per year <small>(<a href="http://www.mayoclinic.org/emr/">Source offiline</a>)</small> and ~90% of physician offices create electronic medical records

- 500 million Tweets per day <small>(<a href="https://www.dsayce.com/social-media/tweets-day/">Source</a>)</small>

- 306 billion emails sent daily in 2020 <small>(<a href="https://techjury.net/blog/how-many-emails-are-sent-per-day">Source</a>)</small>

- Recorded phone calls, blog posts, Facebook updates...

	- ... and that's just the digital stuff

---

### Being able to access and process natural language data is useful

- "Watch Twitter and give me the locations of wildfires, floods, etc, and provide information about damage, shelters and resources in an easy-to-read format"

- "Give me a list of legal cases involving liability for incorrectly wired condominiums in Michigan."

- "Which of these 290 billion emails are likely to be discussing the sale or trafficking of nuclear weapons?"

- "Read the news articles published and tell me everything we know about last night's shooting."

---

### We also directly interact with computers more than ever

- Siri, Google Assistant, Alexa, Cortana, and more

	- "Hey Siri, text my wife that I'm heading home"

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

- They're speed-limited in reading and summarization

- They want things like food, shelter, leisure, and companionship

- They're sources of bias!

---

### So let's enjoy a fantasy...

<img class="big" src="humorimg/fantasea.jpg"> 

---

### You have a computer which understands human language as well as it does computer language

---

<img class="r-stretch" src="img/hal9000.jpg"> 

- (minus the evil)

---

## What could analysis of natural language data do for you?

---

### Speech Recognition

- "Ask people why they're calling, and connect them to the right department based on their answer." 

- "Flag all tech support conversations where the customer mentions a competitor"

- "Transcribe all orders placed at this kiosk"

- "Be Siri, but good."

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

- But LIGN 168 will be a thing next year to learn more about computational speech processing!

---

### Authorship attribution and stylistic analysis

- Examine these two written passages/books and tell me whether they were both written by the same person

- Examine these negative reviews and tell me what demographic the authors likely represent based on the language used.

- Examine every incoming tweet and facebook post and detect posts which seem likely to have been written by robots

---

### Predictive analysis of text

- Look for any information in the newswire which will predict a change in this company's stock price, then buy or sell stock automatically

- Based on all the political posts and tweets in California, how likely is the governor to lose in a recall election?

- Based on this person's Facebook post history, how likely are they to click an ad for weight-loss pills?

	- If you're evil, what if we show them a bunch of fitness posts first?

---

### Automated question answering

- "How far is it from San Diego to Las Vegas?"

- "When did Abe Vigoda actually die?"

- "Where is the chancellor's office on the UCSD campus?"

---

### Command Interpretation

- "Hey Google, turn on the living room lights"

- "Siri, set an alarm for 12:30"

- "Give me a 10 minute timer followed by another 20 minute timer"

- "Set the temperature to 69 degrees"

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

- Look for suicidal ideation, 'suicide notes', or language consistent with mental health crisis, and direct the poster to the [National Suicide Helpline](https://suicidepreventionlifeline.org/talk-to-someone-now/).

- Find anti-vaccination disinformation and remove, label, or provide specific information refuting it

---

<img class="r-stretch" src="comp/covid_candles.jpg">

---

### Text Generation

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

### ... and so much more!

- What other NLP tasks are you familiar with or curious about?

---

Let's dive deeper on two tasks

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

- If monitored words and hashtags appear, show those accounts ads for related products and topics
	
	- Consider the people discussing the topic to be part of the target market
	
	- These people should see Hodinkee content more often

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

	- "My new Dyson really sucks"
	
	- "It sucks that my Roomba doesn't suck anymore"
	
- "Yeah, sure, selling a travel clock during a pandemic is a great idea, \@hodinkee"

---

### Related: Computers don't understand context well

<img class="r-stretch" src="comp/lizard_ceo.jpg">

---

Let's look at one other hard task!

---

## Case Study 2: Temporal Analysis and Event Discovery

---

### Electronic Medical Records

- Many hospitals around the country are switching to Electronic Medical Records (EMRs).

- These records are easily available within the institution, and contain lots of valuable data.

- Creating timelines is incredibly time-consuming for humans, as is comparison.

- What if machines could do this for us?

- [The THYME and RED Projects](https://clear.colorado.edu/TemporalWiki/index.php/Main_Page)

---

### “The patient developed a mild post-surgical rash, which was treated with hydrocortisone at the follow-up.  We'll reevaluate soon.”

- First: Surgery

- Then: Mild rash

- Then: Hydrocortisone, Followup (overlapping)

- Then: No more rash

- Finally: Reevaluate (soon?)

---

### If a computer can be taught to interpret time in medical records, we can ask...

- "I have 30 seconds to learn this patient's history.  Go."

- “How often do patients have heart attacks within 2 years of starting Vioxx?”

- “How many people who have a facelift develop persistent facial numbness?”

- “How long do patients usually live following diagnosis of Glioblastoma?”

- “Is there a correlation between the administration of vaccines and the development of autism?” 

	- **[(No, damnit, those studies were fabricated.)](http://www.webmd.com/brain/autism/news/20110105/bmj-wakefield-autism-faq?print=true)**  

---

### Temporal reasoning is important

- Humans interpret time naturally, and make reference to it often

- Temporality interacts with causality in interesting ways

- Event detection and reasoning is useful in a variety of domains.

- "What happened" is a very fundamental question that everybody wants answered.

---

### What questions could natural language data answer for you?

- Any questions that a human reading it could answer!

---

### I know what you're thinking

<img class="r-stretch" src="img/terminator.png">

---

### ... not so fast

- We're not in too much danger yet!

---

## Why is Natural Language Processing so damned hard?

---

### NLP has all the problems

- Every subfield except phonology has NLP problems

	- Phonology less so because we go straight from speech to written words
	
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

- "I'm so glad you're home with your dog"

- "Siri, play songs by Dead Mouse"

	- "deadmau5"

---

"Bring me the bat, man"

<img class="big" src="naturallanguagedataimg/dugout.jpg"> 

---

"Bring me the Batman"

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

### Understanding Sentences is hard for computers

- "OK Google, turn on the office and bedroom lights"

- "What building houses the Mayor of Boston's Office?"

- "Email the Jessica I'm not married to and tell her I'm gonna be late for our meeting"

---

### Understanding words is hard for computers

- "Sheri has two cats, three dogs, three chickens, a son and two daughters."

	- How many animals does Sheri have?
	
	- How many pets does Sheri have?
	
	- How many children does Sheri have?
	
---

### Understanding the world is hard for computers

- "Hey Siri, set the temperature to 67 degrees"

	- "OK, on which device?"
	
- "Hey Siri, send my wife a text when she gets to the store saying she should buy me donuts because she loves me."

- "Hey Siri, how long is my commute today?"

- "Hey Siri, how long does it take to get from Union Station in LA to Long Beach at 4pm?"

---

### Understanding what words represent is hard for computers

- 'Coreference' or 'Anaphora' is the process of linking words to other words, pronouns, and mentions of them later in discourse

---

### Coreference is difficult

- "Siri, text her back with "OK see you tonight" ''

- “The Bay Harbor Butcher is off the streets, as Dexter Morgan, the alleged killer, was arrested by police over the weekend”

- “Bill Clinton was the President of the United States in 1999.  Now Joe Biden is POTUS.”

- "Siri, send my wife a text saying "On my way home"

- "Alexa, buy me another pair of gray pants."

---

### Understanding temporal expressions is hard for computers

- The process of linking relative dates to absolute, calendar dates and ranges on a timeline

---

### Temporal Expressions can be difficult

- “The bombing occurred 2/13/12 at 0214”

- “Next Tuesday, she’ll come in for a follow-up”

- “She’s been having trouble sleeping lately.”

- “She should expect soreness postoperatively.”

- “TSA regulations have grown increasingly restrictive Post-9/11”

- We expect many Post-COVID disruptions to the supply chain

---

### Understanding temporal relations is hard for computers

- Linking and arranging different events as part of a greater timeline

---

### “The patient developed a mild post-surgical rash, which was treated with hydrocortisone at the follow-up.”

---

### “The patient developed a mild post-surgical rash, which was treated with hydrocortisone at the follow-up, many years after Napoleon's exile to Elba.”

<img class="r-stretch" src="naturallanguagedataimg/napoleonhydro.png">   <!-- .element: class="fragment" --> 

---

### Every event in the history of the universe is temporally related to every other event in this history of the universe.

- ... but we only care about a subset of those at any given moment

	- Relevance is important!

---

### Understanding humans is difficult for computers

- People do not generally provide maximally informative sentences

---

### Doctors hate us.

- “We biopsied the colon, the results were negative”

- “Noted postoperative scarring.”

- “She does not want a colonoscopy, which she had in the 70’s and did not enjoy.”

- “History of Pneumonia, Asthma, h/x diverticulitis, MS”

- “s/p lap appy conv. open, Lungs c/ausc, A&Ox3”

- “Resected Invasive Grade 3 of 4 Adenocarcinoma (AJCC 7th PT4N1bMX).”

---

### Everybody else hates us too

- "Gold covered the miner's hands" and "Gold paid for the miner's education"

- “The Queen of England’s hat was purple”

- “We gave the monkeys the bananas because they were ripe”

- “We gave the monkeys the bananas because they were hungry”

- “Time flies like an arrow, fruit flies like a banana”

- “The old man returned to his house was happy”

---

### What other computer language failures have you seen?

---

### So, computers remain very bad at many parts of human language!

---

### Hooray!

<img class="r-stretch" src="img/morpheus.jpg">

---
 
### Everybody wants to be able to access natural language data and meaning

- "What are people saying about the world?"

- "What do people want?"

- "What's happening in the world right now?"

- "How can we provide better service?"

- "How can we save time by letting machines do the work?"

---

### ... but natural language doesn't want to give it up

- Speech is crazy-complex

- Sentences are difficult to analyze

- Meaning is ridiculous, complex, and depends on knowledge of the world
				
- People assume a lot of knowledge in fellow speakers, and choose not to give all the information

---

### If this kind of work is interesting, consider a Computational Social Sciences Minor!

- <http://css.ucsd.edu>

- Natural Language Processing is an important subpart of CSS, and a neat way to 'tech up' your social science interests

---

### Wrapping up

- Computational Linguistics and NLP are very interesting fields

- There are many great applications for NLP inside and outside linguistics

- Everything that's hard for humans to do is harder for computers to do

- The systems we have are amazingly good, and amazingly bad

---

<huge>Thank you!</huge>