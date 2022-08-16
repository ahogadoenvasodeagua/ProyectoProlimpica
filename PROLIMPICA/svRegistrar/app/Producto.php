<?php
namespace App;
use Illuminate\Database\Eloquent\Model;

class Producto extends Model{

    protected $table = 'modelo_producto';

    protected $fillable=[
        'id', 'nombres', 'precio', 'TipoProduct', 'marca', 'fechaCaducidad', 
    ];

    public $timestamps = false;

    protected $hidden = [
        'id',
    ];
}