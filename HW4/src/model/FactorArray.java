package model;

public class FactorArray<T> implements IArray<T> {

    private Object[] array;
    private int factor;
    private int size;

    public FactorArray(int factor, int initLength) {
        this.factor = factor;
        array = new Object[initLength];
        size = 0;
    }

    public FactorArray() {
        this(50, 10);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void add(T item) {
        if (size() == array.length)
            resize();
        array[size] = item;
        size++;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T)array[index];
    }

    private void resize() {
        Object[] newArray = new Object[array.length + array.length * factor / 100];
        System.arraycopy(array, 0, newArray, 0, array.length);
        array = newArray;
    }

    @Override
    public void add(T item, int index){ 
        resize();
        shift(index);
        array[index]=item;
    }

    // сдвигает с элемента pos на shift элементов 
    //'элементы не влезающие в массив удаляются'
    private void shift(int pos) {
        if (pos>=array.length) return;

        for (int i = array.length-1; i >=pos; i--){
            if (i-1<0){
                return;
            }           
            array[i]=array[i-1];
        }
            
    }

    @Override
    public T remove(int index){         
        Object[] newArray = new Object[size()];
        int shift=0;
        T obj=null;
        for (int i = 0; i <array.length; i++){
            if(i==index){
                obj=(T)array[i];
                continue;
            }
            newArray[shift]=array[i];
            shift=shift+1;
        }
        array=newArray;
        return obj;
    }
}
