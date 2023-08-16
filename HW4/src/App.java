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

        singleArray = new SingleArray();
        vectorArray = new FactorArray();
        factorArray = new VectorArray();
        matrixArray = new MatrixArray();
        oArray = new OArrayList();

        testAddArray(singleArray, 100000);
        testAddArray(vectorArray, 100000);
        testAddArray(factorArray, 100000);
        testAddArray(matrixArray, 100000);
        testAddArray(oArray, 100000);

        System.out.println();
        testGetArray(singleArray, 100000);
        testGetArray(vectorArray, 100000);
        testGetArray(factorArray, 100000);
        testGetArray(matrixArray, 100000);
        testGetArray(oArray, 100000);

        System.out.println();
        testSizeArray(singleArray, 100000);
        testSizeArray(vectorArray, 100000);
        testSizeArray(factorArray, 100000);
        testSizeArray(matrixArray, 100000);

        
        System.out.println();
        testAddRArray(singleArray, 1000);
        testAddRArray(vectorArray, 1000);
        testAddRArray(factorArray, 1000);
        testAddRArray(matrixArray, 1000);
        testAddRArray(oArray, 1000);

        System.out.println();
        testRemoveArray(singleArray, 10000);
        testRemoveArray(vectorArray, 10000);
        testRemoveArray(factorArray, 10000);
        testRemoveArray(matrixArray, 10000);
        testRemoveArray(oArray, 10000);
        
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

    private static void testGetArray(IArray data, int total) {
        long start = System.currentTimeMillis();

        for (int j = 0; j < total; j ++)
            data.get(getRandomNumber(0,data.size()));

        System.out.println(data + " testGetArray: " +
                (System.currentTimeMillis() - start));
    }

    private static void testSizeArray(IArray data, int total) {
        long start = System.currentTimeMillis();

        for (int j = 0; j < total; j ++)
            data.size();

        System.out.println(data + " testSizeArray: " +
                (System.currentTimeMillis() - start));
    }

    private static void testAddRArray(IArray data, int total) {
        long start = System.currentTimeMillis();

        for (int j = 0; j < total; j ++)
            data.add(getRandomNumber(0,10),getRandomNumber(0,data.size()-1));

        System.out.println(data + " testAddRArray: " +
                (System.currentTimeMillis() - start));
    }

    private static void testRemoveArray(IArray data, int total) {
        long start = System.currentTimeMillis();

        for (int j = 0; j < total-1; j ++)
            data.remove(getRandomNumber(0,data.size()-1));

        System.out.println(data + " testRemoveArray: " +
                (System.currentTimeMillis() - start));
    }
}
