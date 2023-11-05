using System.Collections;
using System.Collections.Generic;
using Models;
using UnityEngine;

public class HandController : MonoBehaviour
{
    public GameObject handObject;
    public float offset;

    public float xStart;
    public float yStart;
    public float zStart; 
    public int aantalKaartenZichtbaar;
    private List<Kaart> kaarten;

    private int kijkIndex;

    private List<int> zichtbareKaarten;

    private List<int> geselecteerdeKaarten;

    // Start is called before the first frame update
    void Start()
    {
        var kaarten = new List<Kaart>{
            new Kaart{
                Kleur = 1,
                Rang = 2
            },
            new Kaart{
                Kleur = 2,
                Rang = 10
            },
            new Kaart{
                Kleur = 4,
                Rang = 13
            }
        };
        var selectedPosition = kaarten.Count-1;
    }

    // Update is called once per frame
    // void Update()
    // {
    //     zichtbareKaarten = UpdateZichtbareKaarten();
    //     LoadZichtbareKaarten();
    //     
    // }

    // private List<int> UpdateZichtbareKaarten(){
    //     var result = new List<int>();
    //     if (kaarten.Count<=0) 
    //         return result;
    //     if (kaarten.Count<=aantalKaartenZichtbaar){
    //         for(int i = 0; i++; i < kaarten.Count){
    //             result.Add(i);
    //         }
    //         return result;
    //     }
    // }

    // private void LoadZichtbareKaarten(){
    //     float xposition = xStart;
    //     foreach(Kaart k in zichtbareKaarten){
    //         
    //     }
    // }
}
