//D25,palindrome,stack

#include<iostream>
#include<string.h>
#include<ctype.h>

using namespace std;

class stack{
	public:
	char a[50];//Array for storing input
	char r[50];//Array for storing reverse stack
	int top;
	public:
		stack(){
			top=-1;			
		}
		
		void convert(char[]);
		void push(char);
		void reverse();
		void palindrome();
};


void stack::convert(char str[50]){
	
	int c=0;
	for(int i=0;i<strlen(str);i++){ //strlen() will give the length of str string
		if(isalpha(str[i])){
			str[c]=str[i];
			str[c]=tolower(str[c]);
			c++;
		}
	}
	str[c]='\0'; //'\0' indicate end of the string
	cout<<"Converted string :"<<str<<endl;
}
void stack::push(char c){
	top++;
	a[top]=c;
	a[top+1]='\0';
	cout<<"Stack is pushed by:"<<c<<endl;
}
void stack::reverse(){

	int j=0;
	cout<<endl;
	for(int i=top;i>=0;i--){		
		
		r[j]=a[i];
		cout<<r[j];
		j++;
	}
	r[j]='\0';
}

void stack::palindrome(){
	if(strcmp(r,a)==0)	{  //strcmp() is a function that compares two string
		cout<<"\nString is palindrome";
	}
	else{
		cout<<"\nString is not palindrome";
	}
}

int main(){
	
	stack Stack;
	char str[50];
	int i=0;
	cout<<"Enter string: ";
	cin.getline(str,50);
	
	Stack.convert(str);
    //here str is now converted
	while(str[i]!='\0'){
		Stack.push(str[i]);
		i++;
	}//This will make str a stack
	
	cout<<"Reverse string:";
	Stack.reverse();
	Stack.palindrome();
}


