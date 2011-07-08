/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.5
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */


public class Weight {
  private long swigCPtr;
  protected boolean swigCMemOwn;

  public Weight(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  public static long getCPtr(Weight obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        XapianJNI.delete_Weight(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public String name() {
    return XapianJNI.Weight_name(swigCPtr, this);
  }

  public double getSumPart(long wdf, long doclen) {
    return XapianJNI.Weight_getSumPart(swigCPtr, this, wdf, doclen);
  }

  public double getMaxPart() {
    return XapianJNI.Weight_getMaxPart(swigCPtr, this);
  }

  public double getSumExtra(long doclen) {
    return XapianJNI.Weight_getSumExtra(swigCPtr, this, doclen);
  }

  public double getMaxExtra() {
    return XapianJNI.Weight_getMaxExtra(swigCPtr, this);
  }

  public boolean getSumpartNeedsDoclength() {
    return XapianJNI.Weight_getSumpartNeedsDoclength(swigCPtr, this);
  }

  public boolean getSumpartNeedsWdf() {
    return XapianJNI.Weight_getSumpartNeedsWdf(swigCPtr, this);
  }

}
