# Introduction

This repo contains python code LOOSLY demonstrating the examples shown in the "Architecture Patterns with Python" Book (https://www.cosmicpython.com). The book is an excellent resource for connecting the reasons and tradeoffs of various architecture design patterns commonplace to domain driven designs. I highly recommend buying a copy as an always available reference, personally it's been invaluable.

The main difference between the available source code of the book and this repo is the use of fastapi as the server framework and the use of match case in instances of cascading control flow (e.g. the event bus).

The commits will reflect my journey going back through the book and should roughly correlate with the chapters of the book (taged commits at the end of each chapter). However, I may extend the book and integrate other more opinionated pieces (e.g. NoSQL with boto3 and AWS Dynamo).

## Contributions

Before opening a pull request or working on this repo's code, please open an issue in the github project page. This helps me coordinate who is working on what and start a conversation about if a contribution is in-scope for this repo. Thank you and looking forward to hearing from you.

Note: this repo specifically is for my own learning and will have some opinionate choices (such as development container vs virtual environment and only supporting Python 3.11).