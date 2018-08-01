import os
import csv
from time import strftime
from splinter import Browser

def create_excel():
	with Browser('chrome', headless=True) as browser: #, headless=True
		url = "https://institucional.xpi.com.br/investimentos/" \
			"fundos-de-investimento/lista-de-fundos-de-investimento.aspx"
		browser.visit(url)
		isso = browser.find_by_tag('table')
		tudo = isso.first.html
		final = ''
		flag = False
		for line in tudo.split():
			if line == '<div' or line == '<button':
				flag = True
			if not flag:
				final = final + ' ' + line
			if line ==  "</div>":
				flag = False
			elif '</button>' in line:
				flag = False




		with open('tabela.html', 'w') as file:
			file.write("<table> ")
			file.write(final)
			file.write(" </table>")
			file.close()
		return True

if __name__ == '__main__':
	create_excel()