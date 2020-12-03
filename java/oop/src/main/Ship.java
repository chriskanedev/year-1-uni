public class Ship {

    // add some attributes (variables)
    String name;
    String model;
    Integer maxspeed;
    String owner;
    // add methods to get and set the attributes above

    // add a constructor method:
    public Ship(){ // will your consructor take some initial values?
        this.name="Millennium Falcon";
        this.model="YT-1300F";
        this.maxspeed=1050;
    }

    // add a toString() method:
    public String toString() {
        String shipDetails = "";
        return shipDetails;
    }

    // add getters and setters

    public String getName(){
        return name;
    }

    public String getName(){
        return model;
    }

    public String getOwner(){
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    // add a main() method to instantate (create) a ship object
    // and print it out to the console
    public static void main(String args[]){

    }
}
