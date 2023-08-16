package model;

public class VectorArray<T> implements IArray<T> {

    private Object[] array;
    private int vector;
    private int size;

    public VectorArray(int vector) {
        this.vector = vector;
        array = new Object[0];
        size = 0;
    }

    public VectorArray() {
        this(10);
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
        Object[] newArray = new Object[array.length + vector];
        System.arraycopy(array, 0, newArray, 0, array.length);
        array = newArray;
    }

    @Override
    public void add(T item, int index){ 
        if (size() == array.length)
            resize();

        for (int i = array.length-1; i >index; i--){
            if (i-1<0){
                break;
            }           
            array[i]=array[i-1];
        }

        array[index]=item;
        size++;
    }

    

    @Override
    public T remove(int index){
        T obj=(T)array[index];
        for (int i = index; i <array.length-1; i++){            
            array[i]=array[i+1];
        }
        size--;
        return obj;
    }
}
