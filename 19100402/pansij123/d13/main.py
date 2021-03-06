from modules.stats_word import stats_text_cn as st
import json
from pyquery import PyQuery as pq
import requests as rq
from wxpy import *

bot=Bot()
friends=bot.friends()

@bot.register(friends)

def action(m):
	if m.type == 'Sharing' :
		r=rq.get(m.url)
		q=pq(r.text)
		t=q('#js_content').text()
		print(type(t))
		print(t)

		#-stat words- in t#
		print("Statting cn words...")
		try:
			s = st(t,101)
			#print(s[1:100])
			scores = [ v for k,v in s ] 
			words = [ k for k,v in s ] 
			print(scores)
			print(words)

			def PlotTheStats(scores,words):
			~       fig,ax=plt.subplots()
			~       y_pos=np.arange(len(words))
			~       
			~       ax.barh(y_pos,scores,align='center',color='black',ecolor='black')
			~       ax.set_yticks(y_pos)
			~       ax.set_yticklabels(words)
			~       ax.invert_yaxis()
			~       ax.set_xlabel('Word frequency (1)')
			~       ax.set_title('Frequency of words in message you shared')

			~       plt.savefig("WordStat.png")

			PlotTheStats(scores,words)

			m.reply_image("WordStat.png")
			#return s #equivlent to msg.reply m.reply
		except TypeError:
			print("\nFrom main.py:\tInput should be string if you see an error above")
embed()
