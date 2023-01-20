/**
 * CS 1 22fa
 * Mini Project 8: PokeLife Simulator (Part A)
 * Student name: Julian Navarro
 *
 * Represents a PokePixel instance for the PokeLife game.
 * A PokePixel represents a "Pokemon" object with a type for the game.
 * 
 * TODOs (remove these TODOs from the file comment when done):
 * - A.1 Implement the PokePixel() constructor
 * - A.2 Implement the changeType() setter method
 * - A.3 Implement the getType() getter method
 * - A.4 Implement the toString() method
 */
import java.util.Random;

public class PokePixel {
    // Class constants
    private final String[] TYPES = {"Fire", "Water", "Grass", 
                                    "Electric", "Ground"};
    // Random object for assigning a random type upon initialization 
    private static final Random rand = new Random();

    // Class field
    private String type; 
   
    /**
     * Initializes a PokePixel with a randomly assigned type, from "TYPES".
     */
    public PokePixel() {
        int randIndex = rand.nextInt(TYPES.length);
        String randomType = TYPES[randIndex];
        this.type = randomType;

    }

    /**
     * Changes this PokePixel's type to the provided one
     * (does not do any validation of type String; this is optional).
     * 
     * @param type The type to change the PokePixel to
     */
    public void changeType(String type) {
        this.type = type;
    }

    /**
     * Returns the full type name of this PokePixel
     * 
     * @return The PokePixel type
     */
    public String getType() {
        return this.type;
    }

    /**
     * String representation of this PokePixel, such as "Fir" for "Fire".
     * 
     * @return The first three characters of the type string, to 
     * represent the PokePixel.
     */
    public String toString() {
        String type = getType();
        return type.substring(0,3);
    }
} 
