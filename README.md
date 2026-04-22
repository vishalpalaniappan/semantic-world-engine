# Semantic World Engine (SWE)
This repository provides a Semantic World Engine (SWE) capable of executing fully specified, closed semantic worlds, referred to as designs.

> [!IMPORTANT]
> I made this repo public again after arriving at the same conclusion later. When I made this repo private after adding the note below, it was because I was still trying to understand the relationship between the semantics and the mechanics. Looking back, I had actually arrived at the right answer but I didn't trust it because I still hadn't reached complete clarity in my mind. In the end, I resolved this confusion by understanding that within the context of the semantics, the transformation is meaning being constructed. It is not a black box, it is the canonical construction of meaning in this world. The mechanics are just one possible realization of that meaning, the semantic model is the definition of its correctness. I decided to just leave it as it is without changing anything.

> [!IMPORTANT]  
> I was initially going to delete this repo but then I decided to leave it because this exercise reinforced some ideas in my brain. In trying to build the semantic world engine, I specified the semantics and then I built the state machine. Then I tried to actually realize  the state transformations and I found myself back at the implementation. Then I realized, a semantic world engine is what a program is and I had just gone in a full circle. Except here I made it more explicit the implementation realizes the meaning of the semantic world and I personally found it interesting. There are some interesting tangential ideas I got from this that I would be interested in exploring but anyway, I am just going to leave this as it is.

## Overview

The scope of the intial implementation is limited to the following:
- It contains a sepcification for a closed semantic world
- It executes the state machine specified by the design and performs the  transformations on the world
- It enforces the semantic invariants and flags state transitions that not possible
- It allows the environment to interact with the design

The specification itself is not validated. Here, validation is referring to the actual mechanical consistency off the spec. For example, does a behavior mention a semantic participant that was not defined by the design. These kinds of syntax errors can be easily flagged and I will add that validation in later.

In the future, the validation will be extended to verify the internal consistency of the design, it will check that the axioms of the semantic world are consistent with the requirements of the design and that the graphs produce a realizable internally consistent world. There is ofcourse the problem that the requirements have to be correct, so in that sense, the responsibilty keeps getting passed up the hierarchy. These problems will be tackled later and I will likely do it in the compilation phase.

I don't need to think about those things right now, this current implementation focuses on specifying the semantic world completely so that specification itself can be executed.

# Providing feedback

You can use GitHub issues to [report a bug][bug-report] or [request a feature][feature-req].

[bug-report]: https://github.com/vishalpalaniappan/semantic-world-engine/issues/new?template=bug_report.md
[feature-req]: https://github.com/vishalpalaniappan/semantic-world-engine/issues/new?template=feature_request.md
