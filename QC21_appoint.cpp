
#include <iostream>
using namespace std;

int size;
struct node
{
    float start;
    float end;
    float max;
    float min;
    float flag;
    struct node *next;
}*head;

class appschedule
{
public:
    void createshed();
    void displayshed();
    void bookapp();
    void cancelapp();
    void sortapp();
};

int main()
{
    int ch;
    char ans;
    appschedule A1;

    do
    {
        cout << "\n\n***********MENU***********";
        cout << "\n1. Create Appointment Schedule ";
        cout << "\n2. Display free slots ";
        cout << "\n3. Book an appointment";
        cout << "\n4. Cancel an appointment ";
        cout << "\n5. Sort slotes based on time ";
        cout << "\n6. Exit ";
        cout << " \n Enter your choice";
        cin >> ch;
        switch (ch)
        {
        case 1:
            A1.createshed();
            break;
        case 2:
            A1.displayshed();
            break;
        case 3:
            A1.bookapp();
            break;
        case 4:
            A1.cancelapp();
            break;
        case 5:
            A1.sortapp();
            break;
        case 6:
            exit(0);
            break;
        }
    } while (ch != 6);
}

void appschedule ::createshed()
{
    int i ;
    struct node *temp, *last;
    head =NULL;
    cout<<"\n\n\n How many appointment slots:=";
    cin>>size;
    for(i=0;i<size;i++) 
    {
        temp = new(struct node);
        cout<<"\n\n\t Enter start time :";
        cin>>temp->start;
        cout<<"\n\n\t Enter end duration :";
        cin>>temp->end;
        cout<<"\n\n\t Enter minimum duration :";
        cin>>temp->min;
        cout<<"\n\n\t Enter maximum duration :";
        cin>>temp->max;
        
        temp->flag=0;
        temp->next=NULL;
        if(head==NULL)
        {
            head = temp;
            last = head;

        }
        else{

            last->next = temp;
            last = last->next;

        }

    }
}

void appschedule ::displayshed()
{
    int cnt=1;
    struct node *temp ;
    cout<<"\n\n\t*********appointment schedule*********";
    cout<<"\n\n\t Srno.\tStart\tEnd\tMin.dur\tMax\tStatus";
    temp=head;
    while(temp !=NULL ){
        cout<<"\n\n\t"<<cnt;
        cout<<"\t"<<temp->start;
        cout<<"\t"<<temp->end;
        cout<<"\t"<<temp->min;
        cout<<"\t"<<temp->max;

        if(temp->flag)
            cout<<"\t-booked-";
        else
            cout<<"\t--free--";

        temp= temp->next;
        cnt++;


    }
}
void appschedule::bookapp()
{
    int start;
    struct node *temp;

    cout<<"\n\n\t Please enter appointment time";
    cin>>start;
    temp=head;
    while(temp != NULL)
    {
        if(start==temp->start)
        {
            if(temp->flag==0)
            {
                cout<<"\n\n\t Appointment slot is booked !!!";
                temp->flag=1;

            }
            else 
                cout<<"\n\n\t Appointment slot is not available!!!";

        }
        temp=temp->next;
    }
}
void appschedule::cancelapp()
{
    int start;
    struct node *temp;
    cout<<"\n\n\t Please enter the appointment time to cancel :";
    cin>>start;
    temp=head;

    while(temp !=NULL)
    {
        if(start ==temp->start)
        {
            if(temp->flag==1)
            {
                cout<<" Your appointment is cancelled";
                temp->flag=0;
            }
            else
                cout<<"\n\n\t Your appointment was not booked !!! ";
        }
        temp=temp->next;
    }

}

void appschedule::sortapp(){
    int i,j,val;
    struct node *temp;
    for(i=0;i<size-1;i++){
        temp=head;
        while(temp->next !=NULL)
        {
            if(temp->start>temp->next->start){
                val=temp->start;
            temp->start=temp->start;
            temp->next->start=val;

                 val=temp->end;
            temp->end=temp->next->end;
            temp->next->end=val;

                val=temp->min;
            temp->min=temp->next->min;
            temp->next->min=val;

                val=temp->max;
            temp->max = temp->next->max;
            temp->next->max=val;

            }
            temp=temp->next;
        }
    }
    cout<<"\n\n\t The Appointments got sorted !!! ";
}


