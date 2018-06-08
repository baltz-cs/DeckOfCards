//@baltz_jay @2018
public class driver
{
    public static DeckOfCards dealer = new DeckOfCards();
    public static void main()
    {
        dealer = new DeckOfCards();
        System.out.println("In Order:\n");
        printDeck();
        shuffleDeck();
        System.out.println("\nShuffled:\n");
        printDeck();
    }
    
    public static void printDeck()
    {
        for (int i = 0; i < dealer.deck.length; i ++)
        {
            System.out.println(dealer.deck[i].name);
        }
    }
    
    public static void shuffleDeck()
    {
        dealer.shuffle();
    }
}
