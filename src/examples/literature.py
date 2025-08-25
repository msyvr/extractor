import langextract as lx
from src import extractor
from src.save_and_view import view_tokenization, save_result
import textwrap

def shakespeare(output_dir:str="literature", output_filename:str="results") -> tuple[float, str]:
    """Extract structured data from Shakespearean text."""

    text = textwrap.dedent("""
        Hamlet: "To be, or not to be: that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune,
        Or to take arms against a sea of troubles,
        And by opposing end them? To die: to sleep;
        No more; and by a sleep to say we end
        The heart-ache and the thousand natural shocks
        That flesh is heir to, 'tis a consummation
        Devoutly to be wish'd. To die, to sleep;
        To sleep: perchance to dream: ay, there's the rub;
        For in that sleep of death what dreams may come
        When we have shuffled off this mortal coil,
        Must give us pause: there's the respect
        That makes calamity of so long life;
        For who would bear the whips and scorns of time,
        The oppressor's wrong, the proud man's contumely,
        The pangs of despised love, the law's delay,
        The insolence of office and the spurns
        That patient merit of the unworthy takes,
        When he himself might his quietus make
        With a bare bodkin? who would fardels bear,
        To grunt and sweat under a weary life,
        But that the dread of something after death,
        The undiscover'd country from whose bourn
        No traveller returns, puzzles the will
        And makes us rather bear those ills we have
        Than fly to others that we know not of?
        Thus conscience does make cowards of us all;
        And thus the native hue of resolution
        Is sicklied o'er with the pale cast of thought,
        And enterprises of great pith and moment
        With this regard their currents turn awry,
        And lose the name of action.--Soft you now!
        The fair Ophelia! Nymph, in thy orisons
        Be all my sins remember'd!"
                           
        Juliet: "O Romeo, Romeo, wherefore art thou Romeo?
        Deny thy father refuse thy name, thou art thyself thou not a montegue, 
                           what is montegue? tis nor hand nor foot 
                           nor any other part belonging to a man
        What is in a name?
        That which we call a rose by any other name would smell as sweet,
        So Romeo would were he not Romeo called retain such dear perfection 
                           to which he owes without that title,
        Romeo, Doth thy name!
        And for that name which is no part of thee, take all thyself."
        """
    )

    text_description = "Text from the works of Shakespeare."

    prompt = textwrap.dedent("""                             
    You are an expert at extracting specific information from documents, and an
    expert at deducing implicit aims of example tasks.
    Extract characters, emotions, actions, relationships in the order they appear in the text.
    Provide the output in a structured JSON format based on examples.
    """)

    examples = []
    literature_example = lx.data.ExampleData(
        text="Romeo: But soft! What light through yonder window breaks? It is the East, and Juliet is the sun!",
        extractions=[
            lx.data.Extraction(
                extraction_class="person",
                extraction_text="Romeo",
                attributes={"name": "Romeo"}
            ),
            lx.data.Extraction(
                extraction_class="emotion",
                extraction_text="But soft!",
                attributes={"type":"gentle awe"}
            ),
            lx.data.Extraction(
                extraction_class="person",
                extraction_text="Juliet",
                attributes={"name":"Juliet"}
            ),
            lx.data.Extraction(
                extraction_class="relationship",
                extraction_text="Juliet is the sun",
                attributes={"entity": ["Juliet", "sun"], "type":"metaphor"}
            ),
            lx.data.Extraction(
                extraction_class="relationship",
                extraction_text="Romeo. ... Juliet is the sun!",
                attributes={"entity": ["Romeo", "Juliet"], "type":"affection"}
            ),
            lx.data.Extraction(
                extraction_class="action",
                extraction_text="through yonder window breaks",
                attributes={"type":"transmission"}
            ),
        ]
    )
    examples.append(literature_example)

    result = extractor.extract_data_from_text(text, prompt, examples)
    
    view_tokenization(result)
    save_result(result, text_description, output_dir, output_filename)

    return len(text.encode('utf-8')), text_description
