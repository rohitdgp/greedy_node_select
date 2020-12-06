#include<bits/stdc++.h>
#include<fstream>
#include<iostream>
#include<sstream>
#define ll long long
using namespace std;

int onn[1000],of[1000],n=0;
int vis[1010];
int done[1010];
int show[1010];
int degree[1010];
vector<int> weight;
vector<int> result;

struct data{
    int att,on,off,index;
};

struct data1{
    int act,tot;
    string st;
};

bool cmp(data x,data y){
    if(x.att==y.att) return x.on>y.on;
    return x.att>y.att;
}

int check(vector<int> ch, int matrix[][500])
{
    ll nn=ch.size();
    for(ll i=0;i<nn;i++)
    {
        for(ll j=i+1;j<nn;j++)
        {
            if(matrix[ch[i]][ch[j]]==1)
                return 0;
        }
    }
    return 1;
}

struct compare
{
    inline bool operator() (const data1& a, const data1& b){
        if(a.act==b.act) return a.tot>b.tot;
        return a.act>b.act;
    }
};


void calculate(data a,int matrix[][500])
{
    cout<<endl;
    ll value=a.on;
    vector<data1> each;
    data1 val;
    //cout<<"this is "<<a.att<<endl;
    vector<int> add,status,ch;
    //for(ll i=0;i<n;i++)
      //  if(matrix[a.index][i]==1 && vis[a.index]==1)

    for(ll i=0;i<n;i++)
    {
        if(matrix[a.index][i]==1 && i!=a.index)
        {
            value+=of[i];
            add.push_back(i);
            status.push_back(0);
        }
    }
    cout<<"NODES:  "<<a.index+1;
    for(ll i=0;i<a.att;i++)
        cout<<" "<<add[i]+1;
    cout<<" Tot wt."<<endl;
    //string str;
    stringstream str;
    //sprintf(str,"        2 ");//
    str<<"        2 ";

    //str+=str1.str();
    //str1.str("");
    for(ll j=0;j<a.att;j++)
        {
            str<<status[j]+1<<" ";
            //sprintf(str1,"%d ",status[j]+1);
            //cout<<str1.str()<<endl;
            //str+=str1.str();
            //str1.str("");
            //value+=status[j]?onn[add[j]]:of[add[j]];
        }
    str<<value;
    //str+=str1.str();
    //sprintf(str1,"%d",value);
    //str+=str1;
    val.st=str.str();
    val.act=1;
    str.str("");
    val.tot=value;
    each.push_back(val);
    value=0;
    for(ll i=0;i<pow(2,a.att);i++)
    {
        ch.clear();
        status.clear();
        for(ll j=a.att-1;j>=0;j--)
            status.push_back(0);
        value=a.off;
        ll nval=i;
        for(ll j=a.att-1;j>=0;j--)
        {
            if(nval&1){
                    ch.push_back(add[j]);
                    status[j]=1;
                    //cout<<add[j]<<nval<<" ";
            }
            nval=nval>>1;
        }
        //cout<<endl;
        int cnt=0;
        //if(check(ch,matrix)){
            str<<"        1 ";
            for(ll j=0;j<a.att;j++)
            {
                if(status[j]==1) cnt++;
                str<<status[j]+1<<" ";
                value+=status[j]?onn[add[j]]:of[add[j]];
            }
            str<<value;
            //sprintf(str1,"%d",value);
            //str+=str1.str();
            val.st=str.str();
            val.act=cnt;
            str.str("");
            val.tot=value;
            each.push_back(val);
        //}
    }
    sort(each.begin(),each.end(),compare());
    data1 vari;
    ll no=0,done=0;
    for(ll i=0;i<each.size();i++)
    {
        no=0;
        for(ll j=10,k=0;j<each[i].st.length() && k<add.size();j+=2,k++)
        {
            if(each[i].st[j]=='2' && vis[add[k]]==1)
                no=1;
            if(no==1)
                break;
        }
        if(no==0)
        {
            cout<<each[i].st<<endl;
            if(done==0)
            {
                vari=each[i];
                done=1;
            }
        }
    }
    //ll don=0;
    //cout<<endl;
    //for(ll i=0;i<n;i++)
      //  cout<<vis[i]<<" ";
    //cout<<endl;
    /*for(ll i=0;i<each.size();i++)
    {

        ll no=0;
        ll change=0;
        //cout<<add.size()<<endl;
        if(vis[a.index]==2 && each[i].st[8]==1) change=1;
        for(ll j=10,k=0;j<each[i].st.length()  && k<add.size();j=j+2,k++)
        {
            //cout<<add[k]<<" "<<vis[add[k]]<<endl;
            //cout<<each[i].st[j]<<" ";
            if(each[i].st[j]=='2')
            {
                for(ll l=0;l<n;l++)
                {
                    if(matrix[add[k]][l]==1 and vis[l]==2)
                        change++;
                }
            }

            if(vis[add[k]]==0) continue;
            if(done[add[k]]==1 && vis[add[k]]==1 && each[i].st[j]=='2')
                no=1;
            /*for(ll l=0;l<n;l++)
            {
                if(matrix[add[k]][l]==1 && done[l]==1 && )
            }*/
            //cout<<vis[add[k]]<<" ";
     /*       if(no==1) break;
        }

        if(no==0 && don==0)
        {
            cout<<each[i].st<<endl;
            if(change<each[i].act)
                vari=each[i];
            don=1;
        }
        else if(no==0 && don<5)
        {
            cout<<each[i].st<<endl;
            don+=1;
        }
        //cout<<endl;
    }*/
    //if(vari.st==""){
      //      cout<<"No optimised combination found!!"<<endl;
        //    return;
    //}
    vis[a.index]=vari.st[8]-'0';
    degree[a.index+1]++;
    //coun[a.index]=
    show[a.index]=vis[a.index];
        //result.push_back(a.index);
    for(ll j=10,k=0;j<vari.st.length() && k<add.size();j=j+2,k++)
    {
        if(vis[add[k]]!=vari.st[j]-'0')
            degree[add[k]+1]++;
        vis[add[k]]=vari.st[j]-'0';
        show[add[k]]=vis[add[k]];
        //if(show[add[k]]==1)
          //  done[add[k]]=1;
        //if(vis[add[k]]==2)
        //{
            //result.push_back(add[k]);
            /*for(ll i=0;i<n;i++)
            {
                if(matrix[add[k]][i]==1)
                    vis[i]=1;
            }*/
        //}
    }
    //for(ll i=0;i<n;i++)
    //    cout<<i<<" "<<vis[i]<<endl;
    cout<<"Choosing the most effective case - "<<vari.st<<endl;
}

int main()
{
    memset(show,0,sizeof(show));
    memset(degree,0,sizeof(degree));
     srand(time(NULL));
     ll tot_wt=0,act_wt=0;
     string str;
     ifstream file;

     file.open("NodeDetail.txt");
     getline(file,str);
     getline(file,str);
     while(!file.eof())
     {

         ll i,l=0;
         for(i=0;i<str.length();i++)
         {
             if(str[i]=='w')
                break;
         }
         i+=9;
         for(;i<str.length()-2;i++)
         {
             l=l*10 + str[i]-'0';
             //cout<<l<<endl;
         }
         weight.push_back(l);
         tot_wt+=l;
         getline(file,str);
     }
     file.close();
     file.open("RandomMatrix.txt");
     getline(file,str);
     for(ll k=0;k<str.length();k++)
        if(str[k]=='0' || str[k]=='1') n++;
     cout<<n<<endl;
     int matrix[500][500];
     struct data node[n+2],node1[n+2];
     ll i=0,j=0,cnt=0;
     for(ll k=0;k<str.length();k++)
         {
             if(str[k]=='0'){
                matrix[i][j++]=0;
             }
             if(str[k]=='1'){
                matrix[i][j++]=1;
                cnt++;
             }
         }
     node[i].att=cnt;
     node[i].index=i;
     node[i].on=onn[i]=weight[i];
     node[i].off=of[i]=weight[i]/2;
     while(!file.eof())
     {
         j=0;
         i++;
         cnt=0;
         getline(file,str);
         for(ll k=0;k<str.length();k++)
         {
             if(str[k]=='0'){
                matrix[i][j++]=0;
             }
             if(str[k]=='1'){
                matrix[i][j++]=1;
                cnt++;
             }
         }
         node[i].att=cnt;
         node[i].index=i;
         node[i].on=onn[i]=weight[i];
         node[i].off=of[i]=weight[i]/2;
     }
     file.close();
     for(ll i=1;i<=n;i++)
     {
         degree[i]=node[i-1].att + 2;
     }
     cout<<"  on/off"<<endl;
     for(ll i=0;i<n;i++)
     {
         cout<<node[i].index+1<<" "<<node[i].on<<"/"<<node[i].off<<endl;
     }
     sort(node,node+n,cmp);
     for(ll i=0;i<n;i++)
     {
         node1[i].att=node[i].att;
         node1[i].index=node[i].index;
         node1[i].on=node[i].on;
         node1[i].off=node[i].off;
     }

     memset(vis,0,sizeof(vis));
     memset(done,0,sizeof(done));

     int nn=n;
     i=0;cnt=nn;
     while(cnt)
     {
            //cout<<"step1"<<endl;
             //vis[node1[0].index]=1;
             //while(vis[node[i].index]!=0){i++;}
             if(node[0].att==1) continue;
             calculate(node1[0],matrix);
             done[node1[0].index]=1;
             /*for(ll j=0;j<n;j++)
             {
                 if(matrix[node1[0].index][j]==1)
                    vis[j]=1;
                //cout<<matrix[node1[0].index][j]<<" ";
             }
             //cout<<"step2"<<endl;*/
        //for(ll i=0;i<n;i++)
          //  cout<<done[i]<<" ";
        //cout<<endl;
         cnt=0;
         for(ll i=0,j=0;i<n;i++)
         {
             if(done[node[i].index]==0 && node[i].att>1)
             {
                node1[j].att=node[i].att;
                node1[j].index=node[i].index;
                node1[j].on=node[i].on;
                node1[j].off=node[i].off;
                cnt++;
                j++;
                nn=j;
             }
         }
         //cout<<"cnt="<<cnt<<endl;
         //cout<<"nn - "<<nn<<endl;
         sort(node1,node1+nn,cmp);
         cout<<endl;
     }
     ll no=0;
     vector<int> out;
     for(ll i=0;i<n;i++)
     {
         if(show[i]==0)
         {
             show[i]=2;
         }
     }
     for(ll i=0;i<n;i++)
     {
         for(ll j=0;j<n;j++)
         {
             if(matrix[i][j]==1 && show[i]==2 && show[j]==2)
                if(weight[i]>weight[j]) show[j]=1;
                else show[i]=1;
         }
     }
     for(ll i=0;i<n;i++)
     {
         ll no=0;
         if(show[i]==1){
         for(ll j=0;j<n;j++)
         {
             if(matrix[i][j]==1 && show[j]==1)
                no=0;
             else no=1;
             if(no==1) break;
         }
         if(no==0)
            show[i]=2;
         }
     }
     for(ll i=0;i<n;i++)
        if(show[i]==2)
            out.push_back(i+1);
     cout<<"The final active nodes are - "<<endl;
     /*for(ll i=0;i<result.size();i++)
        {
           for(ll j=0;j<out.size();j++)
                if(result[i]==out[j]) no=1;
            if(no==0) out.push_back(result[i]);
            no=0;
        }*/
    cout<<"No. of nodes - "<<out.size()<<endl<<endl;
    for(ll j=0;j<out.size();j++)
    {
        cout<<out[j]<<" ";
        act_wt+=weight[out[j]-1];
        //cout<<weight[out[j]-1]<<"   ";
    }

    //cout<<endl<<endl<<endl;
    cout<<"\nend"<<endl;
    cout<<out.size()<<endl;
    cout<<tot_wt<<endl;
    cout<<act_wt<<endl;
    ofstream file1;
    file1.open("newalgo_wts.txt");
    for(ll i=1;i<=n;i++)
    {
        file1<<degree[i]<<" ";
    }
    file1<<endl;
    file1.close();
}
