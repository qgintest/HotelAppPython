# Interactive program where you enter ID of item you want to buy
# Input is the csv file
# output is the pDF file indiacting reciept, article and price
# change stock number when bought, optional

import pandas
from fpdf import FPDF


df = pandas.read_csv("articles.csv", dtype={"id": str})

print(df)


class Articles:
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df["id"] == self.id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.id, "price"].squeeze()
        self.stock = df.loc[df["id"] == self.id, "in stock"].squeeze()

    # def get_article_info(self):
    #     return [self.article_id, self.article_name, self.article_price, self.stock]


class Receipt:
    def __init__(self, article, pdf_name):
        self.article = article
        self.name = pdf_name

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr. {self.article.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output(self.name)





# Main code
articleId = input("Choose an article to buy: ")
article = Articles(article_id=articleId)

receipt = Receipt(article, "receipt.pdf")
receipt.generate()