import requests
from pprint import pprint
from bs4 import BeautifulSoup

class Submission:
	def __init__(self,title,link,score,commentCount,commentLink):
		self.title = title
		self.link = link
		self.score = score
		self.commentCount = commentCount
		self.commentLink = commentLink
	def getTitle(self):
		return self.title
	def getLink(self):
		return self.link
	def getScore(self):
		return self.score
	def getCommentCount(self):
		return self.commentCount
	def getCommentLink(self):
		return self.commentLink
		
class Comment:
	def __init__(self,score,text,parent,fullname):
		self.score = score
		self.text = text
		self.parent = parent
		self.fullname = fullname
	def getScore(self):
		return self.score
	def getText(self):
		return self.text
	def getParent(self):
		return self.parent
	def getFullname(self):
		return self.fullname
		
def getSubreddit(sub):
	return requests.get('https://www.reddit.com/r/'+sub)
	
def getSubmissions(sub):
	submissions = []
	soup = BeautifulSoup(getSubreddit(sub).text, 'html.parser')
	titles = []
	links = []
	scores = []
	commentCounts = []
	commentLinks = []
	for elem in soup.find_all('p','title'):
		titles.append(elem.next_element.text)
		links.append(elem.next_element.get('href'))
	for elem in soup.find_all('li','first'):
		commentCounts.append(elem.next_element.text)
		commentLinks.append(elem.next_element.get('href'))
	for elem in soup.find_all('div','score unvoted'):
		scores.append(elem.text)
	for i in range(len(titles)):
		submissions.append(Submission(titles[i],links[i],scores[i],commentCounts[i],commentLinks[i]))
	return submissions
		
def getComments(link):
	soup = BeautifulSoup(requests.get(link+'?sort=top&limit=500').text, 'html.parser')
	texts = []
	scores = []
	parents = []
	names = []
	comments = []
	for elem in soup.find_all('a',{'data-event-action':'permalink'}):
		try:
			texts.append(elem.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.text.encode('ascii','ignore'))
		except:
			texts.append(elem.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element)
	for elem in soup.find_all('span','score unvoted'):
		scores.append(elem.text)
	for elem in soup.find_all('div',{'data-type':'comment'}):
		names.append(elem.get('data-fullname')[3:])
	for elem in soup.find_all('li',{'class':'report-button'}):
		if elem.previous_element == 'parent':
			parents.append(elem.previous_element.previous_element.get('href')[1:])
		else:
			parents.append('None')
	for i in range(len(scores)):
		comments.append(Comment(scores[i],texts[i],parents[i],names[i]))
	return comments
		
if __name__ == '__main__':
	sub = getSubmissions('gaming')
	comments = getComments(sub[2].getCommentLink())
	print(len(comments))
	for comment in comments:
		print(comment.getFullname())