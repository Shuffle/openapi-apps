# Integration Framework
The Integration Framework AI is a BETA app that allows you to do standard actions towards different tools in an agnostic way.  

This app uses AI through large language models, and the app running under the hood uses [Shuffle's Integration Layer API](https://shuffler.io/docs/API#integration-layer).

<img width="421" alt="image" src="https://github.com/Shuffle/openapi-apps/assets/5719530/299252ed-2f2b-4658-8f05-a7386d44f326">

## Why
Most people are not API experts. What this means is that there is a huge demand for self-building workflows that solve problems fast. The most notable easy
problems we see are with simple things like getting and setting data. Shuffle has built out an ontology system on top of apps to make this feasible,
whether or not we know exactly how an app works.

A simple example is the "List Tickets" API, which lists ticket in any Case Management system known to, and tagged by Shuffle.

## Input
The input fields you may need to modify are as follows:
- An App
- An Action
- The fields to send to the App's API with the action

## Using the "Fields" parameter
You can pass either a list of fields, or a dictionary. The App will take care of the rest.

## Cost
There is no additional cost associated with this app. 
It is heavily optimized to use LLM's only when necessary, and not for every request, with it self-learning and fixing itself over time.

## Feedback
Please provide issues you may find associated with the app to support@shuffler.io or through our contact form: [https://shuffler.io/contact](https://shuffler.io/contact) 
