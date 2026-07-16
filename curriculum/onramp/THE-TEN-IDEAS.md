# The Ten Ideas

> **Tier:** Onramp · deeper: [kit/guides/](../kit/guides/) · start of this shelf: [WHY-YOUR-AI-FORGETS.md](WHY-YOUR-AI-FORGETS.md)

Ten ideas, each explained through one everyday picture, each ending with a single sentence
about what it looks like in practice. Read in order or jump around — they stand alone.

## M1 · Resolution ladder

Think of how you actually use a book. You read the **cover** to decide whether to pick it
up. The **table of contents** to decide whether it has your answer. **One chapter** to get
the answer. The **appendix** almost never. Nobody reads the appendix to find out what a
book is about — yet an AI assistant without a ladder does exactly that, front to back,
every time.

So everything the assistant might use is written at several sizes: a one-line entry in a
catalog, a short blurb, a how-to-use-it page, and the full manual. The rule it follows:
read the cheapest version that answers your question, and never skip ahead to a deeper one
without checking the shorter one first.

One warning makes the whole idea work: each size is **written fresh, like a movie trailer**
— a trailer is not the first two minutes of the film. A blurb that's just the manual's
opening paragraph tells you nothing you needed.

*In practice: the assistant answers most questions from the catalog and blurbs, and opens a
full manual only when it's genuinely about to use that skill.*

## M2 · Declarative routing

Picture a street of shops versus a mall directory kiosk. The kiosk has to be updated by
someone, and it's always slightly wrong. The street needs no such person: **each shop hangs
its own sign**, and a new shop opening just… hangs a sign. Nobody asks permission and
nothing central gets edited.

The assistant's abilities work like the shops. Each one carries its own sign — "use me when
the conversation looks like *this*" — and when a task arrives, the assistant reads the
signs and walks into the best match. Adding a new ability means adding it with its sign,
and that's all.

*In practice: the team adds a new procedure on Tuesday and the assistant starts using it
Tuesday, with no central list rewritten and nothing else touched.*

## M3 · Host drivers

A universal travel adapter. Your laptop doesn't care whether the wall socket is British,
European, or Japanese — the adapter absorbs the difference, and the laptop just works.

AI assistants live in different "buildings" — different apps and tools, each with different
sockets: some can search, some can run commands, some can barely read files. Instead of
rewriting the assistant's instructions for each home, there's one set of instructions plus
a small adapter per building. The adapter also says what to do when a socket is missing —
honestly: "you can't search here, so ask the human instead of pretending you searched."

*In practice: the same assistant setup moves from one tool to another without being
rewritten, and it never fakes an ability its current home doesn't have.*

## M4 · Externalized state

A shared project binder, sitting on the table — versus "it's all in Dave's head." When the
project lives in Dave's head, nobody else can check it, nothing survives Dave's vacation,
and when Dave is wrong, the mistake is invisible. When it lives in the binder, anyone can
open it — and anyone can fix it.

The assistant keeps a binder: a one-page note saying what it's working on right now, a
running log of decisions and reasons, and a page of results. The magic is the first page.
If the assistant is focused on the wrong thing, you don't argue with it — **you correct the
page**, the way you'd fix a whiteboard, and it follows the whiteboard.

*In practice: a new session opens with "where were we?" answered from the binder in
seconds, and "what is it doing?" is a page you can read rather than a mystery.*

## M5 · Standing constraints

House rules, posted on the wall. "No shoes inside" doesn't get re-negotiated with every
guest; it's on the wall, it applies to everyone, and pointing at it takes one second.

The assistant gets a short list of posted rules that are always in force — and here's the
craft in it: each rule **names the bad habit it forbids**, the way a doctor names a
condition. "Be concise" is a wish; a named habit with a quick test — *does every sentence
tell the reader something new?* — is checkable. Once a habit has a name, catching it takes
three words instead of a lecture.

*In practice: the corrections you used to repeat every week get names, go on the wall once,
and stop needing to be said.*

## M6 · Boot compilation

Mise en place — the chef's habit. Before service, the station gets prepped: knives here,
towels there, the sauces tonight's menu actually needs. And it's prepped based on **what
last night's service actually used**, not on what the cookbook imagines.

The assistant has a morning-briefing sheet it reads automatically at the start of every
session, before anything else. The discipline is deciding what earns a place on that sheet:
the posted rules, the current project's basics, where the binder is — and nothing else.
Every so often, someone looks at recent sessions and re-packs the sheet: what got used
every day moves in; what nothing touched moves out.

*In practice: sessions start already oriented — no warm-up ritual, no re-explaining — and
the briefing sheet gets sharper every month instead of staler.*

## M7 · In-context ensemble

A panel discussion versus letters in the mail. Put five experts in one room and a question
gets challenged, defended, and refined in an hour — the panelists react to *each other*.
Mail those five experts one at a time and you wait weeks, pay postage per exchange, and
each reply loses the thread a little.

An assistant can hold the panel **inside one sitting**: the skeptic, the optimist, the
accountant, each with a declared point of view, arguing it out where the disagreements are
visible. That beats asking once and getting the mushy average answer — the average of five
opinions tells you nothing about *where they clashed*, and the clash is usually the useful
part.

One honest limit: panelists simulated by one mind share that mind's blind spots. For a
brainstorm, that's fine. For a genuine second opinion — checking work, hunting for what
everyone missed — you want a truly separate reviewer, even though it costs more. Panels
explore; independent reviewers verify.

*In practice: a design decision gets a security view, a cost view, and a maintenance view
in one sitting — and for the final safety check, the team pays for a genuinely independent
look.*

## M8 · Directory-as-object

One labeled folder per client — the way a good office runs. The folder **is** the client
record: its label is the name, its tabs tell you what's inside, and finding out what
clients exist means looking at the shelf. No separate master list that's always out of
date; the shelf is the list.

The assistant's abilities are kept the same way: one folder each, where the folder's label
and tabs say what it is and what it can do. Some folders also work like **templates** — a
folder for "project retrospective" contains the blank form plus a few filled-in examples,
and starting a new one means copying the form, which then collects its own contents.

*In practice: "what can our assistant do?" is answered by looking at the shelf — and
removing an ability is removing a folder, with nothing hidden left behind.*

## M9 · Names as addresses

Tell a good session band "play it Motown" and two words summon a whole tradition — the
bass line, the tambourine, the horns. No sheet music could spell out what those two words
retrieve, because the band already knows Motown. Now imagine instead saying "our Style 7B,"
which means nothing to anyone — you'd have to explain it note by note, every single time.

AI assistants know an enormous amount already. The craft is using the names that unlock
what they know — standard terms, famous examples — instead of inventing private vocabulary
that has to be re-explained forever. And when a team genuinely needs its own term, it gets
defined once, on paper, and then everyone — human and assistant — uses exactly that name.

*In practice: instructions get shorter and work better, because they point at what the
assistant already knows instead of re-teaching it — and no project term ever has two
names.*

## M10 · Tolerant interpretation

A good waiter. You mumble "the, uh… the chicken thing?" and the waiter doesn't lecture you
about menu nomenclature — they figure out you mean the roast chicken, confirm with a nod if
it's ambiguous, and send a **precise** ticket to the kitchen. Sloppy in, exact out. And if
the kitchen's out of something, a good waiter doesn't freeze; they offer the nearest thing
and carry on.

The assistant works the same way: typos, half-remembered names, vague requests — it reads
the intent and proceeds, asking only when the ambiguity actually matters. If a page of its
own binder has gone missing, it recreates a blank one, makes a note, and continues. The
evening keeps moving.

But there's a line, and it matters: the waiter's charity is for *customers*, not for the
kitchen's own recipes. Things the team wrote down — the posted rules, the briefing sheet —
get checked mechanically, because a helpful assistant will otherwise absorb mistakes in
your own paperwork so gracefully that nobody ever notices the paperwork is wrong. (The
original system learned this by shipping a garbled rule sheet for months, invisibly.)

*In practice: sloppy requests just work, small mishaps self-heal — and one small automatic
check keeps the team's own paperwork honest, because charm shouldn't hide broken rules.*

---

## Three habits that run through everything

**The dual-mode contract.** All these written pieces work like directions that serve as GPS
turn-by-turn when the car supports it — and as a printed map when it doesn't. Where
tooling exists to enforce the rules, it enforces them; where it doesn't, the assistant
reads them and follows them anyway. The papers are the same either way. Following-by-
reading is the designed floor, not a broken version.

**The determinism split.** The spreadsheet adds the columns; the accountant decides what
the numbers mean. Anything mechanical and repeatable gets turned into a small automatic
step. The assistant is saved for what actually needs judgment. Never ask the consultant to
do the arithmetic.

**Rewrite, not truncate.** Every short version — the blurb, the briefing line, the catalog
entry — is written fresh for its reader, like a trailer, never chopped off the front of the
long version. It's the least glamorous habit on this page and the one that quietly makes
the ladder worth climbing.

---

*Where this comes from:* these ideas were developed in **MOOLLM** by **Don Hopkins**, who
built them into a playful, explorable world. This page is the plain-clothes version. The
measured claims behind the stories live on the technical shelf, starting at
[the practitioner's kit](../kit/START-HERE.md).
