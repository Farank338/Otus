package model;

import java.util.Arrays;

public class SingleArray<T> implements IArray<T> {

    private Object[] array;

    public SingleArray () {
        array = new Object[0];
    }

    @Override
    public int size() {
        return array.length;
    }

    @Override
    public void add(T item) {
        resize();
        array[size() - 1] = item;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T)array[index];
    }

    private void resize() {
        Object[] newArray = new Object[size() + 1];
        System.arraycopy(array, 0, newArray, 0, size());
        array = newArray;
    }

    @Override
    public void add(T item, int index){         
        resize();
        for (int i = array.length-1; i >index; i--){
            if (i-1<0){
                break;
            }           
            array[i]=array[i-1];
        }

        array[index]=item;
    }

    @Override
    public T remove(int index){     
        //уменьшаем размер на 1    
        Object[] newArray = new Object[size() - 1];
        int shift=0;
        T obj=(T)array[index];
        for (int i = 0; i <array.length; i++){
            if(i==index){
                continue;
            }
            newArray[shift]=array[i];
            shift=shift+1;
        }
        array=newArray;
        return obj;
    }
}
