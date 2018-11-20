## Data Collection
#### TODO

##### Directory Structure
```
./anno
    ./train.json
    ./test.json
./images
    ./test
        ./A
        ./a
        ./..
    ./train
        ./A
        ./a
        ./..
```
#### Annotation json format
```
{
    class: int      // example (0-77)
    image_id: int
    handedness: int // right-handed(0) left-handed(1) 
    gender: int     // male(0) female(1)
    age_group: int  // example (0-7) 
                    // till_6(0), 
                    // from_7_to_16(1), 
                    // from_17_to_25(2), 
                    // from_26_to_35(3), 
                    // from_36_to_45(4) 
                    // from_46_to_55(5)
                    // from_56_to_65(6)
                    // over_66(7)
    page_id: int
}
```
