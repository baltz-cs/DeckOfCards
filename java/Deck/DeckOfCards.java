
/**
 * The deckOfCards object will be implemented in the deckOfCards class
 *
 * @baltz_jay 
 * @2018
 */
public class DeckOfCards
{
    //field - declare array of Card objects with a length of 52 elements
    public Card[] deck = new Card[52];

    // Constructor for objects of class deckOfCards
    public DeckOfCards()
    {
        // for loop through the length of the deck = 52
        for (int i = 0; i < deck.length; i ++)
        {
            deck[i] = new Card(i);
        }
    }
    
    public void shuffle()  //the dealer would use this method to shuffle the cards
    {
        //a temporary card is necessary in the shuffle algorithm
        int N = deck.length;
        for (int i = 0; i < N; i ++)
        {
            int randomIndex = i + (int) (Math.random() * (N-i));
            Card temp = deck[randomIndex];  //temp stores the random card
            deck[randomIndex] = deck[i];    //save the value of the card
            deck[i] = temp;
        }
    }
}
