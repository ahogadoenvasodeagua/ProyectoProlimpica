<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Producto;
use DB;

use Laravel\Lumen\Routing\Controller as BaseController;

class ControladorProducto extends BaseController
{
    public function __construct(){
        return ['nombre'=>'Prolimpia'];
        
    }

    public function all(Request $request){
        $producto = Producto::all();
        //$clientes = Cliente::created("Cliente");
        return response()->json($producto, 200);
        //return response()->json("mensaje"=>"prueba", 200);
        //return ['nombre'=>'Dennis'];
    }
}