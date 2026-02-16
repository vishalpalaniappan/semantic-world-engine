# semantic-world-engine
This repository provides an Semantic World Engine (SWE) for executing closed semantic worlds.

The first version of this tool is limited to the following:
- It contains a sepcification for a closed semantic world
- It executes state machine specified by the design and performs the specified transformations of the world
- It enforces the semantic invariants and flags state transitions that not possible
- It allows the environment to interact with the design

The specification itself is not validated. Here validation is refering to the actual mechanical consistency off the spec, for example, does a behavior mention a semantic participant that was not defined by the design. These kinds of syntax errors can be easily flagged and I will add that validation in later.

In the future, the validation will be extended to verify the internal consistency of the design, it will check that the axioms of the semantic world are consistent with the requirements of the design and that the graphs produce a realizable world. There is ofcourse the problem that the requirements have to be correct, so in that sense, the responsibilty keeps getting passed up the hierarchy. These problems will be tackled later and I will likely do it in the compilation phase.

I don't need to think about those thigns right now, this current implementation focuses on specifying the semantic world completely so that specification itself can be executed.
