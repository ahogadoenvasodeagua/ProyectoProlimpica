<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Cliente;
use DB;

use Laravel\Lumen\Routing\Controller as BaseController;

class ClienteController extends BaseController
{
    public function __construct(){
        return ['nombre'=>'cristian'];
    }
    public function all(Request $request){
        $clientes = Cliente::all();
        return response()->json($clientes,200);
        //return response()->json("mensaje"=>"prueba",200);
        //return ['nombre'=>'cristian'];
    }

}
