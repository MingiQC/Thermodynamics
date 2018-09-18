(* Content-type: application/vnd.wolfram.cdf.text *)

(*** Wolfram CDF File ***)
(* http://www.wolfram.com/cdf *)

(* CreatedBy='Mathematica 11.2' *)

(***************************************************************************)
(*                                                                         *)
(*                                                                         *)
(*  Under the Wolfram FreeCDF terms of use, this file and its content are  *)
(*  bound by the Creative Commons BY-SA Attribution-ShareAlike license.    *)
(*                                                                         *)
(*        For additional information concerning CDF licensing, see:        *)
(*                                                                         *)
(*         www.wolfram.com/cdf/adopting-cdf/licensing-options.html         *)
(*                                                                         *)
(*                                                                         *)
(***************************************************************************)

(*CacheID: 234*)
(* Internal cache information:
NotebookFileLineBreakTest
NotebookFileLineBreakTest
NotebookDataPosition[      1088,         20]
NotebookDataLength[      3607,        100]
NotebookOptionsPosition[      4108,         97]
NotebookOutlinePosition[      4456,        112]
CellTagsIndexPosition[      4413,        109]
WindowFrame->Normal*)

(* Beginning of Notebook Content *)
Notebook[{

Cell[CellGroupData[{
Cell[BoxData[
 RowBox[{"Manipulate", "[", 
  RowBox[{
   RowBox[{"Plot", "[", 
    RowBox[{
     RowBox[{
      RowBox[{"PDF", "[", 
       RowBox[{
        RowBox[{"NormalDistribution", "[", 
         RowBox[{"0", ",", "5"}], "]"}], ",", "x"}], "]"}], "*", 
      RowBox[{"Re", "[", 
       RowBox[{"Exp", "[", 
        RowBox[{"\[ImaginaryI]", " ", "kval", " ", "x"}], "]"}], "]"}]}], ",", 
     RowBox[{"{", 
      RowBox[{"x", ",", 
       RowBox[{"-", "10"}], ",", "10"}], "}"}]}], "]"}], ",", 
   RowBox[{"{", 
    RowBox[{"kval", ",", "1", ",", "30"}], "}"}]}], "]"}]], "Input",
 CellChangeTimes->{{3.746299656775202*^9, 
  3.746299861236206*^9}},ExpressionUUID->"3ef1b1da-1a18-438b-bf10-\
2d6e398feb7a"],

Cell[BoxData[
 TagBox[
  StyleBox[
   DynamicModuleBox[{$CellContext`kval$$ = 26.75, Typeset`show$$ = True, 
    Typeset`bookmarkList$$ = {}, Typeset`bookmarkMode$$ = "Menu", 
    Typeset`animator$$, Typeset`animvar$$ = 1, Typeset`name$$ = 
    "\"untitled\"", Typeset`specs$$ = {{
      Hold[$CellContext`kval$$], 1, 30}}, Typeset`size$$ = {
    360., {109., 113.}}, Typeset`update$$ = 0, Typeset`initDone$$, 
    Typeset`skipInitDone$$ = True, $CellContext`kval$9326$$ = 0}, 
    DynamicBox[Manipulate`ManipulateBoxes[
     1, StandardForm, "Variables" :> {$CellContext`kval$$ = 1}, 
      "ControllerVariables" :> {
        Hold[$CellContext`kval$$, $CellContext`kval$9326$$, 0]}, 
      "OtherVariables" :> {
       Typeset`show$$, Typeset`bookmarkList$$, Typeset`bookmarkMode$$, 
        Typeset`animator$$, Typeset`animvar$$, Typeset`name$$, 
        Typeset`specs$$, Typeset`size$$, Typeset`update$$, Typeset`initDone$$,
         Typeset`skipInitDone$$}, "Body" :> Plot[PDF[
          NormalDistribution[0, 5], $CellContext`x] Re[
          Exp[I $CellContext`kval$$ $CellContext`x]], {$CellContext`x, -10, 
         10}], "Specifications" :> {{$CellContext`kval$$, 1, 30}}, 
      "Options" :> {}, "DefaultOptions" :> {}],
     ImageSizeCache->{411., {155., 161.}},
     SingleEvaluation->True],
    Deinitialization:>None,
    DynamicModuleValues:>{},
    SynchronousInitialization->True,
    UndoTrackedVariables:>{Typeset`show$$, Typeset`bookmarkMode$$},
    UnsavedVariables:>{Typeset`initDone$$},
    UntrackedVariables:>{Typeset`size$$}], "Manipulate",
   Deployed->True,
   StripOnInput->False],
  Manipulate`InterpretManipulate[1]]], "Output",
 CellChangeTimes->{{3.7462997146470537`*^9, 3.7462997263029356`*^9}, 
   3.7462997742858057`*^9, {3.7462998344714203`*^9, 
   3.7462998616580687`*^9}},ExpressionUUID->"bdb3c957-8c3f-446b-b73a-\
ce10958af832"]
}, Open  ]]
},
WindowSize->{759, 601},
WindowMargins->{{Automatic, 292}, {24, Automatic}},
FrontEndVersion->"11.2 for Microsoft Windows (64-bit) (September 10, 2017)",
StyleDefinitions->"Default.nb"
]
(* End of Notebook Content *)

(* Internal cache information *)
(*CellTagsOutline
CellTagsIndex->{}
*)
(*CellTagsIndex
CellTagsIndex->{}
*)
(*NotebookFileOutline
Notebook[{
Cell[CellGroupData[{
Cell[1510, 35, 711, 20, 48, "Input",ExpressionUUID->"3ef1b1da-1a18-438b-bf10-2d6e398feb7a"],
Cell[2224, 57, 1868, 37, 335, "Output",ExpressionUUID->"bdb3c957-8c3f-446b-b73a-ce10958af832"]
}, Open  ]]
}
]
*)

(* End of internal cache information *)

(* NotebookSignature zuTznvdzigOexDKHWun1QNwS *)
