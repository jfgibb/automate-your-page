def get_bullet(description):
    bullet_list = []
    counter = 0
    
    while description.find('BULLET:') != -1:
        next_bullet_start = description.find('BULLET:')        
        next_bullet_end = description.find('BULLET:', next_bullet_start + 1)        
        if next_bullet_end >= 0:
            bullet_list.append(description[next_bullet_start:next_bullet_end -1])
        else:
            bullet_list.append(description[next_bullet_start :])

        description = description[next_bullet_end:]
        counter = counter + 1
    return bullet_list

def generate_concept_HTML(concept_title, concept_description):
    bullets =[]
    bullets = get_bullet(concept_description)
    description = ''
    for n in bullets:
        description = description + '<li>' + n + '</li>'

    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
      <ul>
        ''' + description
    html_text_3 = '''
      </ul>
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description


def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

TEST_TEXT = """TITLE: Stage 2 Overview
DESCRIPTION: BULLET: Manually entering content to create websites is too time consuming BULLET: Stage 2 will introduce the <a href="http://en.wikipedia.org/wiki/Python_%28programming_language%29">Python BULLET:
One important thing to take out of this lesson is to learn to think like a programmer BULLET: The <a href="http://www.sublimetext.com/">Sublime</a> text editor should be used for this lesson BULLET: The lesson will introduce variables and functions that are the heart of programing
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true."""

TOC_TEXT = '''
'''


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
   
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(TEST_TEXT)