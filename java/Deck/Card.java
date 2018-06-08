
/**
 * The Card object will be implemented in the deckOfCards class
 *
 * @baltz_jay 
 * @2018
 */
public class Card
{
    //declare fields
    public int index, value;
    public String suit, face, name, color;
    
    //constructor with parameter i or the index we will be setting up
    public Card(int i)
    {
       index = i;
        
       int quotient = i / 13;  //used to determine the suit
       int remainder = i % 13; //used to determine face and value
       int quotient2 = i / 26; //used to determine color
       
       //the fields will be set using getters or methods that determine the values
       suit = getSuit(quotient);
       face = getFace(remainder);
       color = getColor(quotient2);
       value = getValue(remainder);
       name = getName(face, suit);
    }
    
    public String getSuit(int q)
    {
        switch (q)
        {
            case 0: return "Clubs";
            case 1: return "Spades";
            case 2: return "Hearts";
            case 3: return "Diamonds";
            default: return "Invalid quotient";  //shouldn't be used 
        }
    }
    
    public String getFace(int r)
    {
        switch (r)
        {
            case 0: return "Ace";
            case 1: return "Deuce";
            case 2: return "Three";
            case 3: return "Four";
            case 4: return "Five";
            case 5: return "Six";
            case 6: return "Seven";
            case 7: return "Eight";
            case 8: return "Nine";
            case 9: return "Ten";
            case 10: return "Jack";
            case 11: return "Queen";
            case 12: return "King";
            default: return "Invalid remainder";
        }
    }
    
    public int getValue(int r)
    {
        switch (r)
        {
            case 0: return 14;  //"Ace";
            case 1: return 2;   //"Deuce";
            case 2: return 3;   //"Three";
            case 3: return 4;   //"Four";
            case 4: return 5;   //"Five";
            case 5: return 6;   //"Six";
            case 6: return 7;   //"Seven";
            case 7: return 8;   //"Eight";
            case 8: return 9;   //"Nine";
            case 9: return 10;  //"Ten";
            case 10: return 11; //"Jack";
            case 11: return 12; //"Queen";
            case 12: return 13; //"King";
            default: return 0;
        }
    }
    
    public String getColor(int q)
    {
        //after dividing by 26 the only possible quotients would be 0 and 1
        if (q == 1)
            return "Red";
        else
            return "Black";
    }
    
    public String getName(String face, String suit)
    {
        //this concatenates the face and suit together
        return face + " of " + suit;
    }
    
}
