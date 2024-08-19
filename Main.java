class Animal { void sound() { System.out.println("Animal sound"); } }
class Dog extends Animal { void sound() { System.out.println("Bark"); } }

public class Main {
    public static void main(String[] args) {
        Animal myDog = new Dog(); // Animal reference, Dog object
        myDog.sound(); // Outputs: Bark
    }
}