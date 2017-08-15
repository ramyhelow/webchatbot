"""
Copyright (c) 2016-17 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import logging

from programy.parser.template.nodes.triple import TemplateTripleNode


class TemplateDeleteTripleNode(TemplateTripleNode):

    def __init__(self, subject=None, predicate=None, obj=None):
        TemplateTripleNode.__init__(self, subject, predicate, obj)
        self._node_name = "deletetriple"

    def resolve(self, bot, clientid):
        try:
            resolved = ""
            bot.brain.rdf.delete_entity(self.subject, self._predicate, self.object)
            logging.debug("[%s] resolved to [%s]", self.to_string(), resolved)
            return resolved
        except Exception as excep:
            logging.exception(excep)
            return ""

    def to_string(self):
        return "DELETETRIPLE"

    def to_xml(self, bot, clientid):
        xml = "<deletetriple>"
        xml += self.children_to_xml(bot, clientid)
        xml += "</deletetriple>"
        return xml

    #######################################################################################################
    # DELETETRIPLE_EXPRESSION ::== <deletetriple>TEMPLATE_EXPRESSION</deletetriple>

    def parse_expression(self, graph, expression):
        super(TemplateDeleteTripleNode, self).parse_expression(graph, expression)


