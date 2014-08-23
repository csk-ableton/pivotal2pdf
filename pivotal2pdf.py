from functools import partial
import argparse
from pdf import Pdf
import csv
from util import chunks


type_to_icon_map = {
    'chore': 'icons/chore.png',
    'bug': 'icons/bug.png',
    'feature': 'icons/feature.png'
}


class PivotalStory(object):

    def __init__(self, number, id,
                 title, description,
                 estimate, labels, type,
                 *a, **k):
        super(PivotalStory, self).__init__(*a, **k)

        self.number = number
        self.id = id
        self.title = title
        self.description = description
        self.estimate = estimate
        self.labels = labels
        self.type = type

    def draw(self, pdf, x, y, width, height, show_number=False):
        pdf.set_font('Helvetica')
        pdf.set_text_color(0, 0, 0)
        pdf.set_line_width(0.3)
        pdf.rect(x, y, width, height)

        icon = type_to_icon_map.get(self.type, None)
        if icon is not None:
            pdf.image(icon, x+width-12, y+height-12, 8, 8)

        pdf.set_xy(x+2, y+2)
        pdf.set_font_size(12)
        pdf.multi_cell(width-4, 12, '#' + self.id, align='L', border='B')

        pdf.set_xy(x+2, y+2)
        pdf.multi_cell(width-8, 12, self.estimate, align='R')

        pdf.multi_cell(width, 4)

        pdf.set_x(x+2)
        pdf.set_font('Helvetica', 'B', 18)
        pdf.set_font_size(18)
        pdf.multi_cell(width-4, 8, self.title, align='L')

        pdf.multi_cell(width, 4)

        pdf.set_x(x+2)
        pdf.set_font('Helvetica', '', 12)
        with pdf.clipping_rect(x+2, y, width-4, height-14):
            pdf.multi_cell(width-4, 6, self.description)

        pdf.set_font_size(10)
        pdf.text(x+4, y+height-4, self.labels)

        if show_number:
            pdf.set_font_size(8)
            pdf.set_text_color(150, 150, 150)
            pdf.text(x+width-4, y+height-2, str(self.number))


def make_pivotal_story(column_names, (number, data)):
    return PivotalStory(
        number=number,
        id=data[column_names.index('Id')],
        title=data[column_names.index('Title')],
        description=data[column_names.index('Description')],
        estimate=data[column_names.index('Estimate')],
        labels = data[column_names.index('Labels')],
        type=data[column_names.index('Type')])


def main():
    arg_parser = argparse.ArgumentParser(
        description='Create a pdf document from a exported csv of Pivotal Tracker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    arg_parser.add_argument('csv',
        help='the file path to the csv file')
    arg_parser.add_argument('-m', '--margin', type=int, default=5,
        help='margin of the page in mm')
    arg_parser.add_argument('-o', '--output', default='stories.pdf',
        help='file path to the generated pdf')
    arg_parser.add_argument('-n', '--show-number', action='store_true',
        help='shows the story number on the bottom left')


    args = arg_parser.parse_args()

    page_margin = args.margin
    story_width = (297 - (page_margin*2)) / 2
    story_height = (210 - (page_margin*2)) / 2
    stories = []

    with open(args.csv, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
        stories = map(partial(make_pivotal_story, data[0]),
                      enumerate(data[1:], 1))

    pdf = Pdf()
    pdf.set_auto_page_break(False)

    positions = [
        (page_margin,             page_margin),
        (page_margin+story_width, page_margin),
        (page_margin,             page_margin+story_height),
        (page_margin+story_width, page_margin+story_height)]

    for story_chunk in chunks(stories, 4):
        pdf.add_page('Landscape')
        for story, position in zip(story_chunk, positions):
            story.draw(pdf,
                position[0], position[1],
                story_width, story_height,
                args.show_number)

    pdf.output(args.output)

if __name__ == "__main__":
    main()
