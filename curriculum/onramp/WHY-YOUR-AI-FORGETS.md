# Why Your AI Forgets Everything

> **Tier:** Onramp · deeper: [kit/START-HERE.md](../kit/START-HERE.md)

If you've worked with an AI assistant for more than a week, you know these four
frustrations. They feel like separate problems. They're actually one problem.

**It forgets.** Yesterday you spent an hour explaining the project — what you're building,
what's off-limits, what "done" means. Today it greets you like you've never met. Every
session starts from zero, and you pay the orientation cost again and again — in time, in
money, and in patience.

**It reads everything to find anything.** Ask a small question and watch it churn through
the whole project looking for the answer. Imagine a new employee who, asked where the
stapler is, reads every document in the building.

**It drifts.** You told it — twice — not to touch the billing code, to keep answers short,
to ask before adding anything new. It agreed enthusiastically. Three sessions later it's
doing all three again. Corrections evaporate because there's nowhere for them to live.

**You can't see inside.** When it does something baffling, there's nothing to check. What
was it paying attention to? What did it think the task was? The reasoning happened
somewhere you can't look, and your only tool is to argue with it in chat.

## The one problem underneath

All four frustrations have the same root: **everything the assistant knows lives in the
conversation — and conversations evaporate.** Its knowledge, its instructions, its sense of
what it's working on: all of it is trapped in a chat window with the lifespan of a browser
tab.

The fix is old technology, and you already use it every day: **write things down.**

Not in the chat — in ordinary files that live with the project. What the assistant is
working on: a short note it keeps current. The house rules: posted where it looks at the
start of every session, automatically. Its know-how: a small library with a table of
contents, so it reads the two pages it needs instead of the whole shelf. Its decisions: a
running log, so "why did it do that?" has an answer you can open.

When everything the assistant knows is written down where people can read it, all four
frustrations fall over at once. It stops forgetting, because memory is on paper, and paper
survives the session. It stops reading everything, because there's a table of contents. It
stops drifting, because the rules are posted, not pleaded. And when something goes wrong,
you don't interrogate it — you open the notes, find the wrong line, and fix it. Correcting
a record beats arguing with a mind.

That's the whole approach. The people who built it call the property **legibility** —
everything the assistant knows, a human can read.

## The ten ideas

Making it work took ten specific ideas, each one borrowed from things that already work —
libraries, kitchens, travel adapters, house rules. They have names:

the **resolution ladder** · **declarative routing** · **host drivers** · **externalized
state** · **standing constraints** · **boot compilation** · the **in-context ensemble** ·
**directory-as-object** · **names as addresses** · **tolerant interpretation**

Each gets a page and a picture-in-words in [The Ten Ideas](THE-TEN-IDEAS.md) — about
fifteen minutes, no technical background needed. If you're deciding whether this matters
for your team, [What It Means for a Team](WHAT-IT-MEANS-FOR-A-TEAM.md) is one page. And if
someone hands you an unfamiliar term, the [plain glossary](PLAIN-GLOSSARY.md) has it.

One credit, up front: these ideas come from a system called **MOOLLM**, built by Don
Hopkins — a designer whose earlier work shipped in The Sims. The technical versions live a
few shelves up; this shelf is the view from the ground.
