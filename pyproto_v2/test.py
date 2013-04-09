import ringo
import pdb
import table

#### SIMPLE FUNCTIONALITY TESTING ####
#r = ringo.Ringo()
#r.load('data/comments.xml')
#t = r.tables[0]
#r.wtable = t
#r.select('UserId >= 15')
#r.setWorkingTable('comments')
#r.setWorkingColumn('UserId')
#r.join('comments','UserId')
#r.group('Group','PostId','Score')
#r.dump(100)
#r.order('Order','UserId','PostId')
#r.count('Count','UserId','PostId')
#r.next('UserId','CreationDate','NextId')
#r.unique('UserId','PostId')
#r.setSourceContext()
#r.link('PostId')
#r.makegraph()

#### SAMPLE GRAPHS ####
def QAGraph():
  pdb.set_trace()
  rg = ringo.Ringo()
  rg.load('data/posts.xml')
  rg.setSource('posts','OwnerUserId')
  #rg.setWorkingTable('posts')
  #rg.setWorkingColumn('OwnerUserId')
  rg.label('UserId1')
  rg.select('PostTypeId == 2')
  #rg.setSourceContext()
  rg.link('ParentId')
  rg.join('posts','Id')
  rg.select('PostTypeId == 1')
  rg.link('OwnerUserId')
  rg.label('UserId2')
  rg.group('Group','UserId1','UserId2')
  rg.count('Count')
  rg.select('Count >= 2')
  rg.link('Group')
  rg.unique()
  rg.link('UserId2')
  rg.makegraph()
  rg.dump()

def CommentsGraph():
  rg = ringo.Ringo()
  rg.load('data/comments.xml','data/posts.xml')
  rg.setSource('comments','UserId')
  rg.label('UserId1')
  rg.link('PostId')
  rg.join('posts','Id')
  rg.link('OwnerUserId')
  rg.label('UserId2')
  rg.makegraph()
  rg.dump(30,30)

def CommonComments():
  rg = ringo.Ringo()
  rg.load('data/comments.xml')
  rg.setSource('comments','UserId')
  rg.label('UserId1')
  rg.link('PostId')
  rg.join('comments','PostId')
  rg.link('UserId')
  rg.label('UserId2')
  rg.group('Group','UserId1','UserId2')
  rg.count('Count')
  #rg.select('Count >= 10 && UserId1 != UserId2')
  rg.select('Count >= 10')
  rg.link('Group')
  rg.unique()
  rg.link('UserId2')
  rg.makegraph()
  rg.dump(30,30)

######## DATAFILE NOT AVAILABLE FOR THE MOMENT #######
########     (missing UserId for each vote)    #######
def CommonVoters():
  rg = ringo.Ringo()
  rg.load('data/votes.xml')
  rg.setSource('votes','UserId')
  rg.label('UserId1')
  rg.link('PostId')
  rg.join('votes','PostId')
  rg.link('UserId')
  rg.label('UserId2')
  rg.select('UserId1 != UserId2')
  rg.group('Group','UserId1','UserId2')
  rg.count('Count')
  rg.select('Count >= 10')
  rg.link('Group')
  rg.unique()
  rg.link('UserId2')
  rg.makegraph()
  rg.dump(30,30)

def SameEditors():
  rg = ringo.Ringo()
  rg.load('data/posthistory.xml')
  rg.setSource('posthistory','PostId')
  rg.label('PostId1')
  rg.link('UserId')
  rg.join('posthistory','UserId')
  rg.link('PostId')
  rg.label('PostId2')
  rg.select('PostId1 != PostId2')
  rg.group('Group','PostId1','PostId2')
  rg.unique()
  rg.link('PostId2')
  rg.makegraph()
  rg.dump(30,30)

def Dates():
  rg = ringo.Ringo()
  rg.load('data/posthistory.xml')
  rg.setSource('posthistory','PostId')
  rg.group('FullEdits','CreationDate','PostId')
  rg.unique() # If a user changes different elements (eg, body, title and tags),
              # then there is one row for each element. These two lines group them into one.
  rg.order('Order','UserId','CreationDate')
  rg.group('Group','UserId')
  rg.link('PostId')
  rg.next('Group','Order','NextPostId')
  rg.makegraph()
  rg.dump(30,30)

QAGraph()
#CommentsGraph()
#CommonComments()
#SameEditors()
#Dates()