---
title: Thought Diversity in Software Engineering
subtitle: What, why, how, and why not
---

## Thought Diversity in Engineering
I had a sort of realization about thought diversity a couple days ago. Basically, it boils down to this: it’s a sign of maturity and likeliness to be an effective teammate when a software engineer understands that their voice is not *the correct* voice on their team, but rather *a* voice on the team. Every software engineer will have their biases -- preference towards fast iteration vs. more researched building, ad-hoc vs methodology, abstraction vs explicitness, build in-house vs buy, etc. -- and *there is no correct set of biases*. Every situation has specific and complex requirements, and religious adherence to any one set of principles will inevitably lead to suboptimal decisions and design. Rather, it’s when engineers of differing opinion have productive discussions, and are ultimately willing to yield when appropriate, that good decisions are made. This is similar in character to the idea of ‘strong opinions, weakly held’ -- engineers should have opinions, should have backing reasoning and evidence, and should accept and cherish disagreement from their peers.
Another step along this path is to understand *where* in your team’s ‘thought space’ you typically lie. Are you the foremost voice for fast iteration? Or maybe for increased abstraction? WIth greater awareness of your own and your teammates’ biases, I think it gets easier to understand and guide productive conversations; similarly, understanding which positions are missing from your team’s ‘thought space’ may help reduce the blind spots in your team’s thinking.

## Hiring for Thought Diversity
Reducing cognitive blind spots is I think a good argument for hiring a diverse workforce as well. It follows that a team composed of individuals from diverse backgrounds will have a diverse set of engineering biases to guide their thinking. From my experience, the factors that seem to guide biases most are a.) time of entrance into software engineering and b.) past work experience.

### Time of Entrance into Software Engineering
Software Engineering is, to the dismay of many a crusty Hacker News commenter, an undeniably very fad-driven field. The thought movements popular when an individual is first learning software engineering are often formative down the line. For instance, those coming of age (in a career sense) in the early 2000’s are likely indoctrinated in the benefits of OOP, monoliths, and relational databases. Whereas those entering the field in the late 2010’s (as I did) may feel that the more enlightened approach is a healthy dose of functional style, microservices, and new-fangled noSQL datastores. And this is to say nothing of web development, for which we seem to be iterating in 5 year cycles, unlike the 15 that the rest of the software world seems to live in.
As an aside, I think my workplace is a great example of the confluence between this methodology cycle and the previous. We use Java, by all standards a mainstay of the previous cycle, but the Java we write looks like Go if you squint: lots of interfaces, almost no inheritance, and most models are compiled from protobufs, which are basically structs. It’s a great case study for the benefits of thought diversity on this axis. We get the benefits of a very established language -- stability, performance, tooling -- along with a decade’s worth of software design learnings -- composition over inheritance, separation of data and logic.
An important caveat here: I’m not talking about age here, even though it may sound like I’m alluding to it indirectly. Although age diversity is important for different reasons, it’s not the driving factor here. The biases between an engineer in her 50s and in her 20s, given that both picked up the profession in the late 2010’s, will probably be negligible.

### Work Experience
Previous work experience plays a huge role in the biases one develops, especially around build/buy preference and methodology. This is particularly visible in my workplace, where my coworker who comes from banking is generally the voice of slow, reasoned iteration, while coworkers from Uber, Facebook, and the like are predisposed towards rapid, messier iteration. It’s amusing to hear the same maxims that my roommates (all Googlers fresh out of college) are learning parroted by ex-FAANG coworkers. And as industries go, banking and big tech look like close relatives compared to other areas like academia.
There’s a well-documented tendency to hire people similar to oneself. While this is generally studied from the perspective of gender and race (as it should), it can reasonably be applied to which industry applicants are hired from as well. This is exacerbated by the fact that many hires, especially early on at a company, are referrals, and therefore unlikely to come from separate industries as those already at the company. I think this is something that should be kept in mind for hiring decisions. Hiring an egghead from grad school might seem counterintuitive when the goal is to increase velocity and reliability (“those academics have probably never written a line of production code in their life!”), but in the long term the boost to thought diversity on the team will pay dividends.