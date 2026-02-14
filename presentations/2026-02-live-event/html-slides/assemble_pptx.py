"""
PNG to PowerPoint Assembler
Inserts rendered PNGs as full-slide images with speaker notes for rehearsal.
"""

from pathlib import Path
from pptx import Presentation
from pptx.util import Inches


# Enhanced speaker notes for Presenter View rehearsal.
# Format: WHY this slide matters → WHAT to say → HOW to deliver it.
# Transition cues marked with >>. Key phrases in CAPS for emphasis.
SPEAKER_NOTES = {
    "01-title": (
        "WHY: Set the frame immediately — this talk is NOT about AI tools. "
        "The audience has heard a dozen 'AI will change everything' talks. "
        "You need to differentiate in the first 30 seconds.\n\n"
        "SAY: 'Welcome everyone. Tonight we're talking about something that's "
        "changing how professional services firms operate — not AI tools, but "
        "AI WORKERS. There's a critical difference, and by the end of this "
        "you'll see why it matters for YOUR firm.'\n\n"
        "DELIVER: Confident, conversational. Make eye contact across the room. "
        "Emphasize 'workers' vs 'tools' — this is your thesis."
    ),
    "02-harvest-1800s": (
        "WHY: You're opening with history to build a PATTERN the audience "
        "will recognize later. This isn't nostalgia — it's setup for the "
        "punchline that comes on slides 5-6.\n\n"
        "SAY: 'Let's start with a pattern. In the 1800s, 95% of Americans "
        "worked in agriculture. Harvesting was backbreaking manual labor — "
        "hundreds of workers per farm. This is our baseline.'\n\n"
        "DELIVER: Slow, storytelling pace. Let the image breathe. "
        ">> TRANSITION: 'Then one machine changed everything...'"
    ),
    "03-combine-harvester": (
        "WHY: The combine harvester is the perfect metaphor because it "
        "eliminated the WORK, not the WORKERS. This distinction is the "
        "core thesis of your entire talk. Plant the seed here.\n\n"
        "SAY: 'The combine harvester eliminated 90% of that labor. "
        "But here's the key — the WORK was eliminated. The WORKERS "
        "weren't. They shifted to new roles. Remember this pattern.'\n\n"
        "DELIVER: Punch 'WORK was eliminated, WORKERS weren't' — say it "
        "slowly, let it land. This phrase comes back on the closing slide. "
        ">> TRANSITION: 'Same pattern, different era...'"
    ),
    "04-switchboard-operators": (
        "WHY: Switchboard operators are the KNOWLEDGE WORK example. "
        "Agriculture was physical labor — easy for audience to dismiss. "
        "Switchboard operators used skill, judgment, memory — just like "
        "their senior staff. This makes it personal.\n\n"
        "SAY: 'Bell System employed 350,000 switchboard operators. "
        "This was knowledge work — skill, judgment, memory. Sound familiar? "
        "That's what your senior accountants and attorneys do today.'\n\n"
        "DELIVER: The 'Sound familiar?' is your first direct challenge. "
        "Pause after it. Look at specific people. Let them connect the dots."
    ),
    "05-direct-dial": (
        "WHY: Completing the historical pattern (twice now) so the audience "
        "fully trusts it before you apply it to THEIR firms. Two examples "
        "= pattern. One example = anecdote.\n\n"
        "SAY: 'Automatic switching eliminated all 350,000 jobs. But the "
        "workers adapted — new telecommunications roles. The pattern repeats: "
        "work eliminated, workers adapted. Keep this in mind.'\n\n"
        "DELIVER: Quick, confident. They get the pattern now. "
        ">> TRANSITION: 'Now let's look at YOUR firm today...' "
        "(Shift tone — from history lesson to mirror)"
    ),
    "06-todays-reality": (
        "WHY: THIS is where the talk becomes personal. You're holding up "
        "a mirror. Every person in the room knows their best people waste "
        "time on low-value tasks. This builds tension.\n\n"
        "SAY: 'Your most experienced, most expensive people spend 60% "
        "of their time on repetitive tasks. Invoice coding. Document review. "
        "Status updates. You're paying partner rates for data entry.'\n\n"
        "DELIVER: Slow down on 'partner rates for data entry.' "
        "Let the absurdity land. Some will nod — that's your signal they're with you."
    ),
    "07-million-dollar-bottleneck": (
        "WHY: You're putting a DOLLAR AMOUNT on the problem. Abstract "
        "pain is ignorable. '$2.5M in rework' is not. The '18 months "
        "to rebuild' stat creates urgency — they KNOW people leave.\n\n"
        "SAY: '$2.5 million per year in rework — solving problems someone "
        "already solved. And when a key person leaves? 18 to 24 months "
        "to rebuild their patterns. All that knowledge — locked in their "
        "head, walking out the door.'\n\n"
        "DELIVER: Point to each number on the slide. 'Walking out the door' "
        "should be almost quiet — it's the gut punch."
    ),
    "08-tool-trap": (
        "WHY: Naming what they ALREADY tried (and it failed). This builds "
        "credibility — you're not naive about their past efforts. It also "
        "sets up WHY the tools-vs-workers distinction matters.\n\n"
        "SAY: 'So what did most firms do? Bought ChatGPT licenses for "
        "everyone. Result: 12% adoption, zero process change. Why? "
        "Because tools require a human every single time. No memory, "
        "no autonomy. You hired people, not tools.'\n\n"
        "DELIVER: '12% adoption' with slight head shake. 'You hired "
        "people, not tools' is your bridge to the reframe."
    ),
    "09-what-if-reframe": (
        "WHY: This is the PIVOT of the entire talk. Everything before was "
        "setup. Everything after is the answer. This slide needs to land "
        "like a thunderclap — it's the moment the audience shifts.\n\n"
        "SAY: [2-SECOND PAUSE before speaking] 'What if AI... isn't a tool? "
        "What if it's a WORKER?'\n\n"
        "DELIVER: SLOW. Let silence do the work. This is NOT a transition "
        "slide — it's the most important moment in the deck. Don't rush it. "
        "Hold the pause. Let them sit with the question."
    ),
    "10-workers-vs-tools": (
        "WHY: Making the abstract distinction concrete. The audience needs "
        "to SEE the difference in behavior, not just hear a label change. "
        "Each row is a 'a-ha' moment.\n\n"
        "SAY: 'Here's the difference. Tools: you start every task. Workers: "
        "they run autonomously. Tools: no memory. Workers: they remember "
        "everything. Tools give suggestions. Workers deliver completed work. "
        "This isn't a feature upgrade — it's a category shift.'\n\n"
        "DELIVER: Read each pair as a contrast — gesture left for tools, "
        "right for workers. Let the 'category shift' land at the end. "
        ">> TRANSITION: 'Let me show you what this looks like in practice...'"
    ),
    "11-meet-meridian": (
        "WHY: Moving from theory to PROOF. The audience is thinking 'sounds "
        "nice, but does it work?' Meridian answers that. A 50-person firm "
        "feels relatable — not some Fortune 500 case study.\n\n"
        "SAY: 'Meridian Group — 50-person accounting firm, $10.5 million "
        "revenue. Typical professional services challenges. Could be any "
        "of your firms.'\n\n"
        "DELIVER: Conversational. 'Could be any of your firms' with a "
        "slight nod. You want them to see themselves in this story."
    ),
    "12-five-ai-workers": (
        "WHY: Showing SCOPE — not one pilot, but five real workers doing "
        "real work. Each role is recognizable to the audience. The variety "
        "proves this isn't a narrow solution.\n\n"
        "SAY: 'They deployed 5 AI workers. Not 5 tools — 5 workers. "
        "The invoice processor handles 800 invoices a month. The talent "
        "hunter screens candidates AND schedules interviews without a "
        "human touching it.'\n\n"
        "DELIVER: Walk through each one briefly. Emphasize 'without a "
        "human touching it' — that's what makes it a worker, not a tool."
    ),
    "13-the-numbers": (
        "WHY: CFO slide. Everyone wants to know the ROI. $147K cost vs "
        "$480K value is a clean 3.3x return. The 3.7-month payback "
        "makes it almost riskless.\n\n"
        "SAY: '$147K total cost. $480K value created. Net ROI of $333K "
        "in year one. Payback in 3.7 months. And this is conservative — "
        "it doesn't include quality improvements or the knowledge "
        "preservation we're about to talk about.'\n\n"
        "DELIVER: Let the numbers speak. Point to each metric. "
        "'3.7 months' should get raised eyebrows. 'Conservative' "
        "is your credibility signal — you're not overselling."
    ),
    "14-invoice-processor": (
        "WHY: Deep dive on ONE worker so the audience understands HOW it "
        "actually works. Abstract 'AI does stuff' isn't convincing. "
        "Concrete workflow (email → extract → code → post → flag) is.\n\n"
        "SAY: 'Invoice arrives in email. Data extracted. Coding rules "
        "applied. Posted to QuickBooks. Anomalies flagged for human review. "
        "800 invoices, 120 hours saved, 99.4% accuracy. Better than "
        "human — and it never takes a sick day.'\n\n"
        "DELIVER: Walk the workflow left to right. The '99.4%' and 'sick "
        "day' gets a laugh — use it. Quick energy here."
    ),
    "15-what-really-changed": (
        "WHY: THIS is the deeper insight. The ROI was impressive but "
        "temporary. The 221 PATTERNS are the permanent value. You're "
        "shifting from 'cost savings' to 'institutional capital.' "
        "This is the intellectual heart of the talk.\n\n"
        "SAY: 'But here's what REALLY changed. 221 institutional knowledge "
        "patterns — encoded permanently. When a client mentions year-end, "
        "create a tax planning task. When an invoice exceeds $50K, alert "
        "the partner. These patterns used to live in one person's head. "
        "Now they're institutional capital.'\n\n"
        "DELIVER: Slow down for 'REALLY changed.' Read the examples like "
        "you're quoting from a real system — because you are."
    ),
    "16-three-autonomy-modes": (
        "WHY: Addressing the unspoken fear — 'Will AI go rogue?' No. "
        "YOU calibrate the autonomy. This slide gives the audience "
        "CONTROL, which is what skeptics need to hear.\n\n"
        "SAY: 'You calibrate the autonomy. Invoice coding? Fully autonomous. "
        "Client outreach? Supervised — it drafts, human approves. "
        "Blog posts? Human-led — AI creates the draft, human refines. "
        "You decide the risk tolerance for each task.'\n\n"
        "DELIVER: Emphasize 'YOU calibrate' and 'YOU decide.' "
        "This is about control, not surrender."
    ),
    "17-what-happened-humans": (
        "WHY: Closing the loop on the historical pattern — work eliminated, "
        "workers NOT eliminated. The humans at Meridian are doing BETTER, "
        "higher-value work now. This is the feel-good proof point.\n\n"
        "SAY: 'And the humans? Still there. But now the senior accountant "
        "does client advisory — billable hours up 30%. The recruiter "
        "builds relationships — placements up 40%. Workers freed to do "
        "work only humans can do.'\n\n"
        "DELIVER: Smile here. 'Still there' should be reassuring. "
        "The % gains are proof. This is the promise fulfilled."
    ),
    "18-compounding-effect": (
        "WHY: The compounding argument is what separates this from every "
        "other technology investment. Software depreciates. This "
        "APPRECIATES. That's unique and powerful.\n\n"
        "SAY: 'Month 1: 50 patterns, $15K value. Month 12: 221 patterns, "
        "$40K per month. Each pattern teaches institutional judgment. "
        "This compounds. Unlike a human hire, it only gets better.'\n\n"
        "DELIVER: Trace the growth with your hand — small to large. "
        "'Only gets better' with conviction. "
        ">> TRANSITION: 'Now let's think about what this really means...'"
    ),
    "19-real-asset": (
        "WHY: Reframing AI from an EXPENSE to a CAPITAL INVESTMENT. "
        "Professional services firms think in assets and goodwill — "
        "you're speaking their language. This is the strategic lens shift.\n\n"
        "SAY: 'Your institutional knowledge is capital. It's on your "
        "balance sheet as goodwill — but it's locked in people's heads. "
        "When they leave, you write it off. This isn't about efficiency. "
        "This is about DURABILITY.'\n\n"
        "DELIVER: 'Locked in people's heads' — tap your temple. "
        "'Write it off' — accounting audience knows this pain. "
        "'Durability, not efficiency' is the reframe."
    ),
    "20-capital-lens": (
        "WHY: Giving them TWO metrics to take home. The financial ROI "
        "satisfies the CFO brain. The pattern count satisfies the "
        "strategic brain. Both are real. Both matter.\n\n"
        "SAY: '$333K financial ROI — that's year one. 221 encoded "
        "patterns — that's a permanent asset. The financial ROI is great. "
        "But the knowledge compounds forever.'\n\n"
        "DELIVER: Gesture to each side. 'Compounds forever' with a "
        "slight lean in — this is the money line."
    ),
    "21-scar-tissue-test": (
        "WHY: Making it INTERACTIVE. The audience has been listening — "
        "now they participate. 'Scar tissue' is a visceral metaphor "
        "that makes institutional knowledge tangible and personal.\n\n"
        "SAY: 'Here's a practical exercise. Ask your team tomorrow: "
        "what mistake did we make that we'll never make again? That "
        "answer — that's scar tissue. That's your most valuable "
        "institutional knowledge. That's what you encode first.'\n\n"
        "DELIVER: Make eye contact with specific people. 'Ask your team "
        "tomorrow' makes it an ACTION ITEM. Some will write this down."
    ),
    "22-meridian-examples": (
        "WHY: Concrete examples make the abstract real. Each example "
        "is a story in miniature — a mistake, a lesson, a rule. The "
        "dollar values make them tangible. These are patterns the "
        "audience RECOGNIZES from their own firms.\n\n"
        "SAY: 'Real examples from Meridian. Never send tax estimates "
        "on Fridays — learned after a client panic. Always ask "
        "construction clients about prevailing wage — missed during "
        "an audit. Flag manual journal entries — that's how they caught "
        "fraud. Each one worth $10K to $100K in prevented losses.'\n\n"
        "DELIVER: Read each like a war story. 'Client panic' with a wince. "
        "'Caught fraud' gets attention. Let the dollar range land."
    ),
    "23-ai-changing-fast": (
        "WHY: Preempting the #1 objection. Every audience member is "
        "thinking 'shouldn't we wait for the next version?' You need "
        "to name this objection BEFORE they ask it. That's how you "
        "control the narrative.\n\n"
        "SAY: 'Now I know what you're thinking. But AI is changing "
        "so fast. Should we wait for GPT-6? This thinking mistakes "
        "the asset.'\n\n"
        "DELIVER: Conversational, knowing smile. 'I know what you're "
        "thinking' acknowledges their skepticism. Brief pause before "
        "'mistakes the asset' — then click to the answer."
    ),
    "24-asset-isnt-model": (
        "WHY: The most important strategic argument in the deck. "
        "The model is replaceable. The patterns are permanent. This is "
        "why waiting is a mistake — you're not betting on a model, "
        "you're building an asset.\n\n"
        "SAY: 'The asset isn't the AI model. The asset is your 221 "
        "encoded patterns. The model is just the execution layer. "
        "When GPT-6 launches — upgrade the execution layer. Your "
        "patterns persist. Separation of concerns.'\n\n"
        "DELIVER: This should feel like a revelation. 'Separation of "
        "concerns' will land with technical folks. For others, "
        "'your patterns persist' is the key phrase."
    ),
    "25-like-hiring": (
        "WHY: The hiring analogy makes it safe. Everyone hires people "
        "knowing they might leave. Same logic applies here — but "
        "BETTER because patterns don't quit. Removes the 'what if "
        "the AI platform dies' objection.\n\n"
        "SAY: 'Think of it like hiring. You hire people knowing they'll "
        "leave. The value is work done plus documentation left behind. "
        "AI workers — same logic. But patterns persist forever. No "
        "retirement, no job changes, no knowledge loss.'\n\n"
        "DELIVER: 'No retirement, no job changes, no knowledge loss' "
        "in a rhythmic triple. Let each one land."
    ),
    "26-two-paths": (
        "WHY: Creating URGENCY without being pushy. Path A is clearly "
        "worse but you don't belittle it. You let the audience feel "
        "the competitive pressure themselves. This is the call to action.\n\n"
        "SAY: 'Path A: wait and see. Your competitors encode their "
        "patterns first. You're playing catch-up in 2027. Path B: "
        "start encoding now. Build institutional capital. Compounding "
        "advantage. This is a strategic choice, not a tactical one.'\n\n"
        "DELIVER: Gesture left for Path A (dismissive energy), right "
        "for Path B (lean in). 'Strategic, not tactical' elevates "
        "the decision to the partner level."
    ),
    "27-getting-started": (
        "WHY: Removing the 'it's too complicated' objection. Four "
        "simple steps, clear timeline. Week 1 is almost trivial — "
        "that's intentional. Lower the barrier to action.\n\n"
        "SAY: 'Getting started is simpler than you think. Week 1: "
        "identify one scar tissue pattern. Weeks 2-4: deploy one "
        "AI worker. Then measure, refine, encode the next pattern. "
        "Repeat for 12-18 months. Systematic. Low-risk.'\n\n"
        "DELIVER: Count each step on your fingers. 'Simpler than "
        "you think' with a reassuring tone. 'Systematic. Low-risk.' "
        "are your closing words for this slide — crisp and final."
    ),
    "28-closing-question": (
        "WHY: Bookending with the historical metaphor. The audience "
        "now understands the pattern (work eliminated, workers adapted) "
        "and you're asking them to apply it to THEIR firm. This is "
        "the moment that sticks.\n\n"
        "SAY: [3-SECOND PAUSE — let the room settle]\n"
        "'The harvest was eliminated. The workers weren't.\n"
        "What work will you eliminate?\n"
        "What will your workers do instead?'\n\n"
        "DELIVER: SLOW. Each sentence is its own beat. Don't rush "
        "to fill silence. Hold eye contact. Let the question hang. "
        "After 5 seconds of silence: 'I'd love to hear your questions.' "
        "Hand out business cards during Q&A."
    ),
}


class PowerPointAssembler:
    """Assemble PNG slides into a PowerPoint presentation with speaker notes"""

    def __init__(self, png_dir, output_file):
        self.png_dir = Path(png_dir)
        self.output_file = Path(output_file)
        self.prs = Presentation()
        # Standard 16:9 widescreen
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)

    def add_slide(self, png_file):
        """Add a PNG as a full-slide image with optional speaker notes"""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])  # Blank layout

        slide.shapes.add_picture(
            str(png_file),
            Inches(0), Inches(0),
            width=self.prs.slide_width,
            height=self.prs.slide_height,
        )

        # Add speaker notes if available
        slug = png_file.stem
        if slug in SPEAKER_NOTES:
            slide.notes_slide.notes_text_frame.text = SPEAKER_NOTES[slug]

        return slide

    def assemble_all(self):
        png_files = sorted(self.png_dir.glob("*.png"))
        if not png_files:
            print(f"No PNG files found in {self.png_dir}")
            return False

        print("=" * 60)
        print("POWERPOINT ASSEMBLER")
        print("=" * 60)
        print(f"PNGs:   {self.png_dir}")
        print(f"Output: {self.output_file}")
        print(f"Found {len(png_files)} slides")
        print("=" * 60)

        notes_count = 0
        for png_file in png_files:
            try:
                self.add_slide(png_file)
                has_notes = png_file.stem in SPEAKER_NOTES
                if has_notes:
                    notes_count += 1
                print(f"  [OK] {png_file.name}" + (" + notes" if has_notes else ""))
            except Exception as e:
                print(f"  [X]  {png_file.name}: {e}")

        self.output_file.parent.mkdir(parents=True, exist_ok=True)
        self.prs.save(str(self.output_file))

        print(f"\nCOMPLETE: {len(self.prs.slides)} slides, {notes_count} with speaker notes")
        print(f"Saved to: {self.output_file}")
        return True


def main():
    base = Path(__file__).parent
    assembler = PowerPointAssembler(
        png_dir=base / "output",
        output_file=base.parent / "output" / "AI-Workforce-Deck.pptx",
    )
    success = assembler.assemble_all()
    if success:
        print(f"\n[OK] Open in PowerPoint -> Presenter View to see speaker notes")
    else:
        print("\n[X] Assembly failed")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
