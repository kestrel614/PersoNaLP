### 2017 Apr 2
### Yuqiong Li
### This document summarizes main features of ready-to-use chatbot engines


# Intro and basics of bots

## What a Bot Engine wraps inside
Understanding the user intent
Decide the bot's response
Decide the bot's action
Decide if the bot ask questions
### Stories
Two schools - Rules vs Machine Learning

1. Machine learning
- problem lies in training dataset
- using a dozen examples can work well
- but for medium complexity need thousands conversations

2. Rules or imperative approach
- script or program
- good = instant demos - the bot will work
- bad = new paths -- add more rules until collapses
- the curse of combinatorics - eg. new rule conflicts with old rules



# MicroSoft Bot Framework
## Comments
- Probably one of the most comprehensive ones?

[Official documentation](https://docs.botframework.com/en-us/)
### Elements in the kit
- Bot Builder SDK(software development kit) - in
  - C# [Source Codes](https://github.com/Microsoft/BotBuilder/tree/master/CSharp)
  - Node.js
- Bot Connector
- Developer Portal
- Bot Directory

### Features
Powerful dialog system with dialogs that are isolated and composable.
Built-in dialogs for simple things like Yes/No, strings, numbers, enumerations.
Built-in dialogs that utilize powerful AI frameworks like LUIS
Bots are stateless which helps them scale.
Form Flow for automatically generating a Bot from a C# class for filling in the class and that supports help, navigation, clarification and confirmation.




# Facebook - Bots for Messenger
Example product - Facebook M
- language: Node.js
- API: on Facebook

## engine: wit.ai (sold to Facebook in 2015)
[Official website](https://wit.ai/blog/2016/04/12/bot-engine)
- HTTP API, Python, Node.js, Ruby







# ChatScript
## Comments
one of the smaller companies; Question - how does this compare to MS and FB?

## Features
- a rule-based nlp engine
- language: C and C++
- Opensource on [git](https://github.com/bwilcox-1234/ChatScript)
## Usage
- installation `git clone https://github.com/bwilcox-1234/ChatScript`
- input = text script file
## Resource
- [wiki](https://github.com/bwilcox-1234/ChatScript/blob/master/WIKI/README.md)



# Pandora Bot
## Comments
one of the smaller companies; Question - how does this compare to MS and FB?
## Features
- Pricing: 9/mo for developers 1000 interactions
- Language: Node.js; Python; Java
- Haven't looked into features as seem to be a closed kit?



# A list of other companies not so helpful but doing similar things. Products in packages
## [Imperson](http://imperson.com)
## Rebot.me
