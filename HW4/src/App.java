import model.*;

import java.util.Date;

public class App {
    
    public static void main(String[] args) throws Exception {
        IArray singleArray = new SingleArray();
        IArray vectorArray = new FactorArray();
        IArray factorArray = new VectorArray();
        IArray matrixArray = new MatrixArray();
        IArray oArray = new OArrayList();




        testAddArray(singleArray, 100000);
        testAddArray(vectorArray, 100000);
        testAddArray(factorArray, 100000);
        testAddArray(matrixArray, 100000);
        testAddArray(oArray, 100000);

        System.out.println(singleArray.get(0)+" "+singleArray.get(1)+" "+singleArray.get(2));
        System.out.println(vectorArray.get(0)+" "+vectorArray.get(1)+" "+vectorArray.get(2));
        System.out.println(factorArray.get(0)+" "+factorArray.get(1)+" "+factorArray.get(2));
        System.out.println(matrixArray.get(0)+" "+matrixArray.get(1)+" "+matrixArray.get(2));
        System.out.println(oArray.get(0)+" "+oArray.get(1)+" "+oArray.get(2));

        singleArray.add(-1, 1);
        vectorArray.add(-1, 1);
        factorArray.add(-1, 1);
        matrixArray.add(-1, 1);
        oArray.add(-1, 1);

        System.out.println();
        System.out.println(singleArray.get(0)+" "+singleArray.get(1)+" "+singleArray.get(2));
        System.out.println(vectorArray.get(0)+" "+vectorArray.get(1)+" "+vectorArray.get(2));
        System.out.println(factorArray.get(0)+" "+factorArray.get(1)+" "+factorArray.get(2));
        System.out.println(matrixArray.get(0)+" "+matrixArray.get(1)+" "+matrixArray.get(2));
        System.out.println(oArray.get(0)+" "+oArray.get(1)+" "+oArray.get(2));

        singleArray.remove(1);
        vectorArray.remove(1);
        factorArray.remove(1);
        matrixArray.remove(1);
        oArray.remove(1);

        System.out.println();
        System.out.println(singleArray.get(0)+" "+singleArray.get(1)+" "+singleArray.get(2));
        System.out.println(vectorArray.get(0)+" "+vectorArray.get(1)+" "+vectorArray.get(2));
        System.out.println(factorArray.get(0)+" "+factorArray.get(1)+" "+factorArray.get(2));
        System.out.println(matrixArray.get(0)+" "+matrixArray.get(1)+" "+matrixArray.get(2));
        System.out.println(oArray.get(0)+" "+oArray.get(1)+" "+oArray.get(2));
        
    }
    public static int getRandomNumber(int min, int max) {
        return (int) ((Math.random() * (max - min)) + min);
    }

    private static void testAddArray(IArray data, int total) {
        long start = System.currentTimeMillis();

        for (int j = 0; j < total; j ++)
            data.add(getRandomNumber(0,10));

        System.out.println(data + " testAddArray: " +
                (System.currentTimeMillis() - start));
    }
}
