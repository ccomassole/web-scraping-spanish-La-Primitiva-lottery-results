<p align="center"><img width="690" height="308" src="https://github.com/ccomassole/web-scraping-spanish-lottery-results/blob/master/pdf/loteriaprimitiva.jpg"></p>
<h2>LoteriaPrimitivaResults</h2>
First Experience of web scraping. Developing a script for results extraction of Spanish’s La Primitiva lottery from the Official Website: <a href="https://www.loteriasyapuestas.es">Loterias y Apuestas del Estado</a>.
<h2>Members</h2>
The task has been carried out individually by Cesar Comas Sole.
<h2>Context</h2>
The goal of this web scraping project is to create a service that allows the periodic extraction of the results of the Spanish’s La Primitiva lottery to later on automatically check the winners of the resale lotto service of our hypothetical customer, a football fan club.
For each update, our customer will update the info in their digital publications (facebook, twitter and web), offering value to its members.
The draws of La Primitiva take place on Thursdays (9:40 pm) and Saturdays (9:40 pm). El Gordo de la Primitiva (which is a Premium draw) is raffled on Sunday (9:30 p.m.).
The official website where the La Primitiva results are published is <a href="https://www.loteriasyapuestas.es">Loterias y Apuestas del Estado</a> which belongs to a Spanish Government Company.
<h2>Contents</h2>
<p>The data extracted is stored into a CSV file with the following fields:</p>
<p><ul>
  <li>Lottery: 'Classic', 'ElGordo'</li>
  <li>Date: Date of the draw</li>
  <li>Winner_Num_1: First winning number</li>
  <li>Winner_Num_2: Second winning number</li>
  <li>Winner_Num_3: Third winning number</li>
  <li>Winner_Num_4: Fourth awarded number</li>
  <li>Winner_Num_5: Fifth winning number</li>
  <li>Winner_Num_6: Sixth winning number (only Classic Mode)</li>
  <li>Complementary: Complementary number (only Classic Mode)</li>
  <li>Refund: Number that allows the reimbursement of the value of the ticket bet</li>
  <li>Joker: Set of 6 ordered digits associated with an extraordinary prize (only Classic Mode)</li>
</ul></p>
For the purpose of this project, data of the draws have been extracted between the following dates: 4/8/18 - 11/27/18, as the goal is not the extraction of a large volume of information, but the execution of a script that automates weekly processes.
<h2>Acknowledgments</h2>
We thank SELAE (Sociedad Española de Loterias y Apuestas del Estado), as the owner of the data, the use of the information extrated from their site.
<h2>Inspiration</h2>
We have been inspired by a friend startup who created a service to expand the Lottery gaming into neighborhood associations.
<h2>License</h2>
<p><b>This code is shared under the license: CC0: Public domain license</b></p>
<h2>Resources</h2>
<p>[1] Richard Lawson (2015), “Web Scraping with Python”. Chapter 1. Ed. Packt Publishing</p>
<p>[2] L.Subirats, M.Calvo. (2018), "Web Scraping". UOC</p>
<p>[3] Corey Schafer. YouTube. <a href="https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g">Corey Schafer Channel </a></p>
<p>[4] ttguayco. GitHub Repo. <a href="https://github.com/tteguayco/Web-scraping">Web Scraping</a></p>
